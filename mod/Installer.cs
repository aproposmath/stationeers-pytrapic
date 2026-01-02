using System;
using System.IO;
using System.IO.Compression;

using Cysharp.Threading.Tasks;
using System.Threading;

using StationeersLaunchPad;

namespace StationeersPyTrapIC;

public class PythonWorkspace
{
    public static string CacheDir => Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
    public static string WorkspaceDir => Path.Combine(CacheDir, "ws");
    public static string VersionFile => Path.Combine(WorkspaceDir, "pytrapic_version.txt");
    public static string VenvDir => Path.Combine(WorkspaceDir, $".venv");
    public static string PythonExe => Path.Combine(VenvDir, "python.exe");
    public static string PipExe => Path.Combine(VenvDir, "Scripts", "pip.exe");
    public static bool IsInitialized => File.Exists(VersionFile) && File.ReadAllText(VersionFile).Trim() == PyTrapICPlugin.PluginVersion;


    private static SemaphoreSlim _initLock = new SemaphoreSlim(1);

    public static async UniTask InitWorkspace(bool forceReinstall = false)
    {
#if DEBUG
      return;
#endif
        // check if already installed
        if (IsInitialized && !forceReinstall)
        {
            L.Debug("Python workspace already installed and up to date");
            return;
        }

        await _initLock.WaitAsync();

        // double check inside lock
        if (IsInitialized && !forceReinstall)
            return;

        // remove existing workspace recursively
        if (Directory.Exists(WorkspaceDir))
        {
            L.Debug("Removing existing Python workspace");
            Directory.Delete(WorkspaceDir, true);
        }

        L.Info("Installing Python workspace");

        Github.Repo repo = new Github.Repo("aproposmath", "stationeers-pytrapic");
        var versionTag = "v" + PyTrapICPlugin.PluginVersion;
#if DEBUG
        versionTag = "dev";
#endif
        var initialRelease = await repo.FetchTagRelease(versionTag);
        if (initialRelease == null)
        {
            L.Error($"Could not find release for tag {versionTag}");
            throw new Exception($"Could not find release for tag {versionTag}");
        }

        var asset = initialRelease.Assets.Find(a => a.Name == "ws.zip");
        if (asset == null)
        {
            L.Error("Could not find ws.zip asset in release");
            throw new Exception("Could not find ws.zip asset in release");
        }

        var archive = await asset.FetchToMemory();
        archive.ExtractToDirectory(CacheDir);

        // write version.txt
        File.WriteAllText(VersionFile, PyTrapICPlugin.PluginVersion);

        L.Info("Python workspace installation complete");
    }
}
