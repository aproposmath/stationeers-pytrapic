namespace StationeersPyTrapIC;

using System.IO;
using System;
using System.Text;

using System.Linq;
using System.Diagnostics;
using System.Collections.Generic;


using Newtonsoft.Json;

using Assets.Scripts.UI;
using Assets.Scripts.Objects;
using Assets.Scripts.Objects.Pipes;

public class LogicDataExtractor
{
    static readonly string TypesFile = Path.Combine(PythonWorkspace.CacheDir, "pytrapic_types_data.json");

    public static void ExtractAndBuild(bool force = false)
    {
        if (!force && !HasLogicDataChanged())
            return;

        try
        {
            var typesData = ExtractLogicData();
            File.WriteAllText(TypesFile, typesData);

            var pyExe = PythonWorkspace.PythonExe;
            var sw = Stopwatch.StartNew();
            Process.Start(new ProcessStartInfo(pyExe, $"-m stationeers_pytrapic.build_types {TypesFile}") { UseShellExecute = false }).WaitForExit();
            var buildTime = sw.ElapsedMilliseconds;
            L.Debug($"Building structures_generated.py took {buildTime}ms");
        }
        catch (Exception ex)
        {
            L.Error($"Failed to rebuild logic data: {ex}");
            L.Error($"{ex.StackTrace}");
            File.Copy(PythonWorkspace.StructuresBackupFile, PythonWorkspace.StructuresFile);
            if (File.Exists(TypesFile))
                File.Delete(TypesFile);
            throw;
        }
    }

    public static bool HasLogicDataChanged()
    {
        var newData = ExtractLogicData();
        if (!File.Exists(TypesFile)) return true;
        var oldData = File.ReadAllText(TypesFile);
        return newData != oldData;
    }

    public static string ExtractLogicData()
    {
        var stopwatch = Stopwatch.StartNew();
        StringBuilder sb = new();
        TextWriter tw = new StringWriter(sb);
        using var writer = new JsonTextWriter(tw);
        writer.WriteStartObject();
        writer.WritePropertyName("version");
        writer.WriteValue(typeof(Stationpedia).Assembly.GetName().Version.ToString());
        writer.WritePropertyName("pages");
        writer.WriteStartArray();

        var prefabHashes = new HashSet<int>();

        foreach (var page in Stationpedia.StationpediaPages)
        {
            var hash = page.PrefabHash;
            var prefab = Prefab.Find(hash);
            if (prefab is not ILogicable) continue;
            prefabHashes.Add(hash);
        }

        List<int> sortedPrefabHashes = [.. prefabHashes.OrderBy(h => h)];

        foreach (var hash in sortedPrefabHashes)
        {
            var prefab = Prefab.Find(hash);
            var name = prefab.PrefabName;
            var key = "Thing" + name;
            var page = Stationpedia.Instance.GetPage(key);

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
        stopwatch.Stop();
        L.Debug($"Logic data extraction took {stopwatch.ElapsedMilliseconds}ms");
        return sb.ToString();
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
