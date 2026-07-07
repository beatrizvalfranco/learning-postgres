provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

resource "google_service_account" "dbt" {
  account_id   = "dbt-647"
  display_name = "dbt"
}

locals {
  dbt_project_roles = [
    "roles/bigquery.jobUser",
    "roles/bigquery.dataEditor",
    "roles/storage.objectAdmin",
  ]
}

resource "google_project_iam_member" "dbt_roles" {
  for_each = toset(local.dbt_project_roles)

  project = var.project
  role    = each.value
  member  = "serviceAccount:${google_service_account.dbt.email}"
}

resource "google_service_account" "terraform" {
  account_id   = "terraform"
  display_name = "terraform"
}

locals {
  terraform_project_roles = [
    "roles/compute.networkAdmin",
    "roles/resourcemanager.projectIamAdmin",
    "roles/iam.serviceAccountAdmin",
    "roles/serviceusage.serviceUsageAdmin",
    "roles/storage.admin",
    "roles/bigquery.admin",
  ]
}


resource "google_project_iam_member" "terraform_roles" {
  for_each = toset(local.terraform_project_roles)

  project = var.project
  role    = each.value
  member  = "serviceAccount:${google_service_account.terraform.email}"
}