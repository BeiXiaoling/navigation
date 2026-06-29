from pathlib import Path
import shutil
import time

conf_path = Path("/opt/1panel/apps/openresty/openresty/conf/conf.d/www.ovo-s.com.conf")
snippet_path = Path("/tmp/admin-openresty-locations.conf")

conf = conf_path.read_text(encoding="utf-8")
snippet = snippet_path.read_text(encoding="utf-8").rstrip() + "\n"

backup_path = conf_path.with_suffix(conf_path.suffix + "." + time.strftime("%Y%m%d%H%M%S") + ".bak")
shutil.copy2(str(conf_path), str(backup_path))

start_marker = "    # BEGIN navigation admin\n"
end_marker = "    # END navigation admin\n"
block = start_marker + snippet + end_marker

if start_marker in conf and end_marker in conf:
    start = conf.index(start_marker)
    end = conf.index(end_marker, start) + len(end_marker)
    new_conf = conf[:start] + block + conf[end:]
else:
    insert_at = conf.rfind("\n}")
    if insert_at == -1:
        raise SystemExit("Could not find server block closing brace")
    new_conf = conf[:insert_at] + "\n" + block + conf[insert_at:]

conf_path.write_text(new_conf, encoding="utf-8")
print("backup=" + str(backup_path))
