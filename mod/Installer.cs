using System;
using System.IO;
using System.IO.Compression;

using Cysharp.Threading.Tasks;
using System.Threading;
using UnityEngine.Networking;
using Newtonsoft.Json;

namespace StationeersPyTrapIC;

public class PythonWorkspace
{
    public static string CacheDir => Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
    public static string WorkspaceDir => Path.Combine(CacheDir, "ws");
    public static string VenvDir => Path.Combine(WorkspaceDir, $".venv");
    public static string SitePackagesDir => Path.Combine(VenvDir, "Lib", "site-packages");
    public static string PythonExe => Path.Combine(VenvDir, "python.exe");
    public static string PipExe => Path.Combine(VenvDir, "Scripts", "pip.exe");

    public static string TypingsDir => Path.Combine(WorkspaceDir, "typings");

#if DEBUG
    public static string VersionTag => "main";
#else
    public static string VersionTag => "v" + ThisModInfo.Version;
#endif
    public static string VersionFile => Path.Combine(WorkspaceDir, "pytrapic_version.txt");
    public static bool IsInitialized => File.Exists(VersionFile) && File.ReadAllText(VersionFile).Trim() == VersionTag;

    public const string WorkspaceVersionTag = "v0.2.3"; // manually increase this if some dependencies change
    public static string WorkspaceVersionFile => Path.Combine(WorkspaceDir, "pytrapic_ws_version.txt");
    public static bool IsWorkspaceInitialized => File.Exists(WorkspaceVersionFile) && File.ReadAllText(WorkspaceVersionFile).Trim() == WorkspaceVersionTag;

    private static readonly SemaphoreSlim _initLock = new(1);

    private static async UniTask<ZipArchive> FetchZip(string url)
    {
        using (var downloadRequest = UnityWebRequest.Get(url))
        {
            L.Info($"Downloading {url}");
            var downloadResult = await downloadRequest.SendWebRequest();

            if (downloadResult.result != UnityWebRequest.Result.Success)
            {
                L.Error($"Failed to download {url}! result: {downloadResult.result}, error: {downloadResult.error}");
                return null;
            }

            var data = downloadRequest.downloadHandler.data;
            L.Debug($"Downloaded {data.Length} bytes");
            var stream = new MemoryStream(data.Length);
            stream.Write(data, 0, data.Length);
            stream.Position = 0;

            return new ZipArchive(stream);
        }
    }


    public static async UniTask FetchAndExtract(string versionTag, string assetName, string extractDir)
    {
        var url = $"https://api.github.com/repos/aproposmath/stationeers-pytrapic/releases/tags/{versionTag}";
        using var request = UnityWebRequest.Get(url);
        request.SetRequestHeader("User-Agent", "UnityWebRequest");
        var response = await request.SendWebRequest();

        if (response.result != UnityWebRequest.Result.Success)
        {
            L.Error($"Failed to fetch release info! result: {response.result}, error: {response.error}");
            throw new Exception($"Failed to fetch release info for tag {versionTag}");
        }

        var json = JsonConvert.DeserializeObject<Newtonsoft.Json.Linq.JObject>(request.downloadHandler.text);
        var assetUrl = (string)json.SelectToken($"$.assets[?(@.name == '{assetName}')].url");

        if (assetUrl == null)
        {
            L.Error($"Could not find asset ${assetName} in release ${versionTag}");
            throw new Exception($"Could not find asset ${assetName} in release ${versionTag}");
        }

        var archive = await FetchZip(assetUrl);
        archive.ExtractToDirectory(extractDir);
    }

    public static async UniTask InitWorkspace(bool forceReinstall = false)
    {
        // check if already installed
        if (IsWorkspaceInitialized && !forceReinstall)
        {
            L.Debug("Python workspace already installed and up to date");
            return;
        }

        try
        {
            await _initLock.WaitAsync();

            // double check inside lock
            if (IsInitialized && !forceReinstall)
                return;

            if (!Directory.Exists(CacheDir))
                Directory.CreateDirectory(CacheDir);

            // remove existing workspace recursively
            if (Directory.Exists(WorkspaceDir))
            {
                L.Debug("Removing existing Python workspace");
                Directory.Delete(WorkspaceDir, true);
            }

            L.Info("Installing Python workspace");

            await FetchAndExtract(WorkspaceVersionTag, "ws.zip", CacheDir);

            File.WriteAllText(WorkspaceVersionFile, WorkspaceVersionTag);

            L.Info("Python workspace installation complete");
        }
        finally
        {
            _initLock.Release();
        }
    }

    public static async UniTask InitPytrapic(bool forceReinstall = false)
    {
        await InitWorkspace();

        if (IsInitialized && !forceReinstall)
            return;

        try
        {
            await _initLock.WaitAsync();

            foreach (var dir in Directory.GetDirectories(SitePackagesDir, "stationeers_pytrapic*", SearchOption.TopDirectoryOnly))
                Directory.Delete(dir, true);

            if (Directory.Exists(TypingsDir))
                Directory.Delete(TypingsDir, true);

            await FetchAndExtract(VersionTag, "stationeers-pytrapic.whl", SitePackagesDir);
            await FetchAndExtract(VersionTag, "typings.zip", WorkspaceDir);

            File.WriteAllText(VersionFile, VersionTag);
            L.Info("PyTrapIC installation complete");
        }

        finally
        {
            _initLock.Release();
        }
    }
}
