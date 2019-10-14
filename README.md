# DMS upload tool

## How to run this tool?

Run the following command

**On Windows:**
```docker run --rm -d -p 5000:5000 -v %cd%\storage:/storage registry.gitlab.com/um-cds/projects/vwdata/dms-storage```

**On Unix/Linux/macOS:**
```docker run --rm -d -p 5000:5000 -v %(pwd)/storage:/storage registry.gitlab.com/um-cds/projects/vwdata/dms-storage```