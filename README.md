# Newsletter
1. Run terraform init
2. Run terraform apply
3. Add ses_txt_record to your DNS records
    Type: "TXT"
    Host: "@" (or leave blank depending on Squarespace’s requirements)
    Value: Copy the 'ses_txt_record.value' from the ses_txt_record output.
    TTL: "3600"
4. Add each record from ses_dkim_records, add to DNS records
    Type: "CNAME"
    Host: Copy the 'name' from record
    Value: Copy the 'value' from record
    TTL: "3600"

5. Check back in AWS console until `Identity status` = "Verified"
    SES > Identities > Check `Identity Status` for your identity  

6. Check back in AWS console until `DKIM configuration` = "Verified"
    SES > Identities > {your identity} > Check the `DKIM configuration` status

7. Create a Service Limit Increase case on AWS
    https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase
    Fill out the form and wait for AWS to respond. Without this step you won't be able to send emails outside of your domain. Search SES sandbox vs. production for more info.