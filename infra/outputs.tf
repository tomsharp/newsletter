output "ses_txt_record" {
  value = {
    name  = "@"
    type  = "TXT"
    value = "amazonses:${aws_ses_domain_identity.this.verification_token}"
    ttl   = 3600
  }
}

output "ses_dkim_records" {
  value = [
    for dkim in aws_ses_domain_dkim.this.dkim_tokens : {
      name  = "${dkim}._domainkey"
      type  = "CNAME"
      value = "${dkim}.dkim.amazonses.com"
      ttl   = 3600
    }
  ]
}