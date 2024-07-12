provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg1" {
  name     = "rg-myapp-prod"
  location = "East US"
}

resource "azurerm_virtual_network" "Vnet1" {
  name                = "vnet-myapp-prod"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_subnet" "snet1" {
  name                 = "snet-myapp-prod"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_key_vault" "KV1" {
  name                        = "kv-myapp-prod"
  location                    = azurerm_resource_group.example.location
  resource_group_name         = azurerm_resource_group.example.name
  sku_name                    = "standard"
  tenant_id                   = "your-tenant-id"
  purge_protection_enabled    = true
  network_acls {
    default_action             = "Deny"
    bypass                     = "AzureServices"
    virtual_network_subnet_ids = [azurerm_subnet.example.id]
  }
}

resource "azurerm_key_vault_secret" "secret1" {
  name         = "secret-myapp"
  value        = "super-secret-value"
  key_vault_id = azurerm_key_vault.example.id
}

resource "azurerm_private_endpoint" "privateEP1" {
  name                = "privateEP-myapp-prod"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  subnet_id           = azurerm_subnet.example.id

  private_service_connection {
    name                           = "privatesc-myapp-prod"
    is_manual_connection           = false
    private_connection_resource_id = azurerm_key_vault.example.id
    subresource_names              = ["vault"]
  }
}
