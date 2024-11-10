# Create the service account
resource "google_service_account" "general_service_account" {
  account_id   = "general-sa"
  display_name = "General Service Account"
}

# Assign multiple roles to the service account
locals {
  service_account_roles = [
    "roles/artifactregistry.admin",   # Artifact Registry Admin
    "roles/run.admin",                # Cloud Run Admin
    "roles/cloudsql.client",          # Cloud SQL Client
    "roles/clouddeploy.admin",        # Cloud Deploy Admin
    "roles/cloudbuild.builds.editor",  # Cloud Build Editor
    "roles/iam.serviceAccountUser", # Cloud Run Impersonation
  ]
}

resource "google_project_iam_member" "service_account_roles" {
  for_each = toset(local.service_account_roles)  # Use each role in the locals list
  project  = var.PROJECT_ID
  role     = each.key
  member   = "serviceAccount:${google_service_account.general_service_account.email}"
}