terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.1"
    }
  }
}
resource "local_file" "example" {
  content  = var.message
  filename = "${path.module}/output.txt"
}
