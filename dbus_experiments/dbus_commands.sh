# List available method calls for the system
dbus-send --system            \
  --dest=org.freedesktop.DBus \
  --type=method_call          \
  --print-reply               \
  /org/freedesktop/DBus       \
  org.freedesktop.DBus.ListNames

# List all methods exposed by systemd
dbus-send --system --type=method_call --print-reply \
      --dest=org.freedesktop.systemd1 \
      /org/freedesktop/systemd1 \
      org.freedesktop.DBus.Introspectable.Introspect

