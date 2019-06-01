# PREX
> The r"^(P)ython (R)egular (Ex)pression \3tractor$"

## Vision
### TODO

General feature set:
- [ ] Add unique/deduplication mode
- [ ] Add config file for formatters (-c CONFIG)
- [ ] Add template support (-t TEMPLATE)
- [ ] Add variables to input (filename, path, etc.)

Formatters:
- [ ] Add CSV formatter

## Installation

```sh
sudo ln -s /path/to/prex.py /usr/sbin/prex
```

## Usage

```sh
prex [-i FILE] [-f FORMAT] REGEXP
```

If `FILE` is not specified, `STDIN` is used.
That way, data can be easily piped into prex.

Output formats: `plain (default), json`

### Examples

Use with pipe:
```sh
echo "Hello" | prex ".*"
```

Use with file:
```sh
prex -i /var/log/foo.log ".*"
```
