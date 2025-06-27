output "storage_account_name" {
  value = azurerm_storage_account.archive.name
}

output "archive_function_endpoint" {
  value = azurerm_function_app.archive_function.default_hostname
}

output "restore_function_endpoint" {
  value = azurerm_function_app.restore_function.default_hostname
}
