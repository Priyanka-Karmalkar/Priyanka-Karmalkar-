provider "azurerm" {
  features = {}
}

resource "azurerm_storage_account" "archive" {
  name                     = "billingarchive${random_string.suffix.result}"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  access_tier              = "Cool"
}

resource "azurerm_function_app" "archive_function" {
  name                       = "ArchiveOldRecordsFunction"
  location                   = var.location
  resource_group_name        = var.resource_group_name
  app_service_plan_id        = azurerm_app_service_plan.plan.id
  storage_account_name       = azurerm_storage_account.archive.name
  storage_account_access_key = azurerm_storage_account.archive.primary_access_key
  version                    = "~4"
}

resource "azurerm_function_app" "restore_function" {
  name                       = "RestoreRecordFunction"
  location                   = var.location
  resource_group_name        = var.resource_group_name
  app_service_plan_id        = azurerm_app_service_plan.plan.id
  storage_account_name       = azurerm_storage_account.archive.name
  storage_account_access_key = azurerm_storage_account.archive.primary_access_key
  version                    = "~4"
}
