variable "subscription_id" {
  description = "Azure Subscription ID"
}

variable "client_id" {
  description = "Azure Client ID"
}

variable "client_secret" {
  description = "Azure Client Secret"
}

variable "tenant_id" {
  description = "Azure Tenant ID"
}

variable "resource_group_name" {
  description = "Resource Group Name"
  default     = "pythwebpostgresql-rg"
}

variable "location" {
  description = "Azure Location"
  default     = "East US"
}

variable "aks_cluster_name" {
  description = "AKS Cluster Name"
  default     = "pythwebpostgresql-aks"
}

variable "node_count" {
  description = "Number of nodes in the AKS cluster"
  default     = 1
}
