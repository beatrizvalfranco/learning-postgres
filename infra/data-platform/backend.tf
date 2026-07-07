terraform {
  backend "gcs" {
    bucket = "movies-datalake-terraform-state"
    prefix = "terraform/state/data-platform"
  }
}