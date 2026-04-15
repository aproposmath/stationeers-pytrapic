using System.IO;
using System.Diagnostics;
using System.Collections.Generic;


using Newtonsoft.Json;

using Assets.Scripts.UI;
using Assets.Scripts.Objects;
using Assets.Scripts.Objects.Pipes;

namespace StationeersPyTrapIC;

public class LogicDataExtractor
{
    public static void ExtractAndBuild()
    {
        var typesFile = Path.Combine(PythonWorkspace.CacheDir, "pytrapic_types_data.json");
        ExtractLogicData(typesFile);

        var pyExe = PythonWorkspace.PythonExe;
        
        // run python -m stationeers_pytrapic.build_types typesFile
        var process = Process.Start(new ProcessStartInfo(pyExe, $"-m stationeers_pytrapic.build_types {typesFile}") { UseShellExecute = false });
        // wait for the process to finish
        process.WaitForExit();
    }
    
    public static void ExtractLogicData(string outputFile)
    {
        StreamWriter sw = new(outputFile);
        using var writer = new JsonTextWriter(sw);
        writer.WriteStartObject();
        writer.WritePropertyName("version");
        writer.WriteValue(typeof(Stationpedia).Assembly.GetName().Version.ToString());
        writer.WritePropertyName("pages");
        writer.WriteStartArray();
        foreach (var page in Stationpedia.StationpediaPages)
        {
            page.ParsePage();

            var name = page.PrefabName;
            var prefab = Prefab.Find(name);
            if (prefab is not ILogicable) continue;

            var key = page.Key;

            writer.WriteStartObject();
            writer.WritePropertyName("Key");
            writer.WriteValue(key);
            writer.WritePropertyName("PrefabName");
            writer.WriteValue(name);
            writer.WritePropertyName("PrefabHash");
            writer.WriteValue(prefab.PrefabHash);
            writer.WritePropertyName("LogicInfo");
            writer.WriteValue(true);

            WriteLogicInsert(writer, page.LogicInsert, "LogicInsert");
            WriteLogicInsert(writer, page.LogicSlotInsert, "LogicSlotInsert");
            WriteLogicSlotInsert(writer, page);
            
            writer.WriteEndObject();
        }
        writer.WriteEndArray();
        writer.WriteEndObject();
    }

    public static void WriteLogicInsert(JsonTextWriter writer, List<StationLogicInsert> data, string name)
    {
        writer.WritePropertyName(name);
        writer.WriteStartArray();
        foreach (var insert in data)
        {
            writer.WriteStartObject();
            writer.WritePropertyName("LogicName");
            writer.WriteValue(insert.LogicName);
            writer.WritePropertyName("LogicAccessTypes");
            writer.WriteValue(insert.LogicAccessTypes);
            writer.WriteEndObject();
        }
        writer.WriteEndArray();
    }
    
    public static void WriteLogicSlotInsert(JsonTextWriter writer, StationpediaPage page)
    {
        writer.WritePropertyName("SlotInserts");
        writer.WriteStartArray();
        foreach (var insert in page.SlotInserts)
        {
            writer.WriteStartObject();
            writer.WritePropertyName("SlotName");
            writer.WriteValue(insert.SlotName);
            writer.WritePropertyName("SlotIndex");
            writer.WriteValue(insert.SlotIndex);
            writer.WriteEndObject();
        }
        writer.WriteEndArray();
    }
}
