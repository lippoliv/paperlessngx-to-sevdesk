# PaperlessNGX to sevDesk

Poll new files from PaperlessNGX and push them to sevDesk as new voucher.

## Configuration

The following environment variables are used for configuration

| Name                                 | Description                                                                   |
|--------------------------------------|-------------------------------------------------------------------------------|
| RUN_INTERVAL                         | How often to scan for new files                                               |
| PAPERLESSNGX_URL                     | The PaperlessNGX url (e.g. `https://paperle.ss`)                              |
| PAPERLESSNGX_TOKEN                   | The PaperlessNGX token to be used for fetching new files                      |
| PAPERLESSNGX_FILTER_TAG_ID           | **Optional:** The PaperlessNGX tag (ID) to filter documents for               |
| PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID | **Optional:** The PaperlessNGX document type (ID) to filter documents for     |
| SEVDESK_TOKEN                        | **Optional:** The sevDesk token to be used for uploading files (default: 300) |
