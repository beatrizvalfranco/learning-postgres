provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

resource "google_storage_bucket" "movies_datalake_bronze" {
  name     = "movies-datalake-bronze"
  location = "US"

  force_destroy               = false
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}

resource "google_bigquery_dataset" "bronze" {
  dataset_id    = "bronze"
  friendly_name = "bronze"
  description   = "External tables over raw API data in GCS"
  location      = "US"

  labels = {
    layer = "bronze"
  }
}

resource "google_bigquery_dataset" "silver" {
  dataset_id    = "silver"
  friendly_name = "silver"
  description   = "Cleaned, typed, deduplicated tables derived from bronze data"
  location      = "US"

  labels = {
    layer = "silver"
  }
}

resource "google_bigquery_dataset" "gold" {
  dataset_id    = "gold"
  friendly_name = "gold"
  description   = "Analytics-ready views for BI and reporting"
  location      = "US"

  labels = {
    layer = "gold"
  }
}