variable "project" { 
    type = string
}

variable "sa_dbt" { 
    type = string
}

variable "sa_terraform" { 
    type = string
}

variable "region" {
  type = string
  default = "us-central1"
}

variable "zone" {
  type = string
  default = "us-central1-c"
}