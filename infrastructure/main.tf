locals {
  services = [
    "frontend",
    "backend"
  ]
}

resource "google_cloud_run_v2_service" "default" {
  for_each = toset(local.services) 
  name     = "${each.key}-cloudrun-service" 
  location = var.REGION
  project = var.PROJECT_ID
  # deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}

# Create artifact registry
resource "google_artifact_registry_repository" "applications" {
  location      = var.REGION
  repository_id = "applications"
  description   = "applications docker repository"
  format        = "DOCKER"

}

# create cloud sql database
resource "google_sql_database_instance" "main" {
  name             = "main-instance"
  database_version = "POSTGRES_15"
  region           = var.REGION

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = "db-f1-micro"
  }
}