using System;
using System.Diagnostics;
using System.IO;
using System.Text;

namespace StationeersPyTrapIC;

public class PythonVenv
{
    public const string PYTHON_VERSION = "3.14.2";
    public static string CacheDir => Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
    public static string VenvDir => Path.Combine(CacheDir, $"venv");
    public static string PythonExe => Path.Combine(VenvDir, "python.exe");
    public static string PipExe => Path.Combine(VenvDir, "Scripts", "pip.exe");
    public static string VersionFile => Path.Combine(VenvDir, "pytrapic_version.txt");
    public static bool IsPythonInitialized => File.Exists(VersionFile) && File.ReadAllText(VersionFile).Trim() == PyTrapICPlugin.PluginLongVersion;
    public static bool IsInitialized => File.Exists(VersionFile) && File.ReadAllText(VersionFile).Trim() == PyTrapICPlugin.PluginLongVersion;

    public static void UpdatePythonModules()
    {
        var proc = new ProcessStartInfo
        {
            FileName = PipExe,
            Arguments = "install --cache_dir pip_cache pygments astroid luaparser parso basedpyright",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true,
            WorkingDirectory = CacheDir
        };

        var process = Process.Start(proc);
        process.WaitForExit();
        var output = process.StandardOutput.ReadToEnd();
        var error = process.StandardError.ReadToEnd();
        if (process.ExitCode != 0)
        {
            L.Error($"Error updating Python modules: {error}");
            throw new Exception($"Error updating Python modules: {error}");
        }
        L.Info("Updated Python modules:\n" + output);
    }

    public static void InstallPython()
    {
        Timer t = new Timer("InstallPython");

        L.Info("Installing Python and dependencies");
        var pythonZipName = $"python-{PYTHON_VERSION}-embed-amd64.zip";
        var pythonUrl = $"https://www.python.org/ftp/python/{PYTHON_VERSION}/{pythonZipName}";
        var pipUrl = $"https://bootstrap.pypa.io/get-pip.py";
        var cacheDir = Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
        Directory.CreateDirectory(VenvDir);
        var pythonZipPath = Path.Combine(cacheDir, pythonZipName);
        using (var client = new System.Net.WebClient())
            client.DownloadFile(pythonUrl, pythonZipPath);
        System.IO.Compression.ZipFile.ExtractToDirectory(pythonZipPath, VenvDir);

        using (var client = new System.Net.WebClient())
            client.DownloadFile(pipUrl, Path.Combine(VenvDir, "get-pip.py"));

        var pythonVersion = PYTHON_VERSION
            .Substring(0, PYTHON_VERSION.LastIndexOf('.'))
            .Replace(".", "");

        File.AppendAllText(
            Path.Combine(VenvDir, $"python{pythonVersion}._pth"),
            "\nimport site\n",
            Encoding.UTF8
        );

        var pipInstallCmd = new ProcessStartInfo
        {
            FileName = PythonExe,
            Arguments = "get-pip.py",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true,
            WorkingDirectory = VenvDir
        };

        var proc = Process.Start(pipInstallCmd);
        proc.WaitForExit();
        var error = proc.StandardError.ReadToEnd();
        if (proc.ExitCode != 0)
        {
            L.Error($"Error installing pip: {error}");
            throw new Exception($"Error installing pip: {error}");
        }

        L.Info($"Installed Python {PYTHON_VERSION} to {VenvDir}");
        t.Dispose();
    }


    public static void Init(bool forceReinstall = false)
    {
#if DEBUG
        // I'm using symlinks to the python sources for development
        return;
#endif
        try
        {
            if(forceReinstall)
              L.Info("Forcing Python venv reinstallation");
            bool needReinstall = forceReinstall || !IsInitialized;

            if (!needReinstall)
                return;

            if (Directory.Exists(VenvDir))
            {
                L.Info($"Deleting existing Python venv at {VenvDir}");
                Directory.Delete(VenvDir, true);
            }

            InstallPython();
            PythonVenv.UpdatePythonModules();
            File.WriteAllText(VersionFile, PyTrapICPlugin.PluginLongVersion);
        }
        catch (Exception ex)
        {
            L.Error(ex.StackTrace);
            L.Error($"Error initializing PythonVenv: {ex}");
        }
    }
}
