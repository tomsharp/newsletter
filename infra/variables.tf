variable "region" {
    description = "AWS region"
    type = string
    default = "us-east-1"
}
variable domain {
    description = "Domain to send emails from. e.g., yourdomain.com"
    type = string
}