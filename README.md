# Priyanka-Karmalkar-
# Azure Cosmos DB Cost Optimization with Archival Strategy

azure-cosmosdb-cost-optimization/
├── README.md
├── architecture-diagram.png
├── terraform/
│   ├── main.tf
│   └── variables.tf
├── function-app/
│   ├── ArchiveOldRecordsFunction/
│   │   ├── __init__.py
│   │   └── function.json
│   └── RestoreRecordFunction/
│       ├── __init__.py
│       └── function.json
└── scripts/
    └── archive_data.py
