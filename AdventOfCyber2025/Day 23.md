# AWS Security  - S3cret Santa 

## Learning Objectives

- Learn the basics of AWS accounts.
- Enumerate the privileges granted to an account, from an attacker's perspective.
- Familiarise yourself with the AWS CLI.


Q1) Run `aws sts get-caller-identity`. What is the number shown for the "Account" parameter?

```
ubuntu@tryhackme:~$ aws sts get-caller-identity
{
    "UserId": "7l2m2bp70u09jrhqr7rp",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/sir.carrotbane"
}
```

A1) `123456789012`

Q2) Which IAM component is used to describe the permissions to be assigned to a user or a group?

A2) `policy`

Q3) What is the name of the policy assigned to `sir.carrotbane`?

Command used: `aws iam list-user-policies --user-name sir.carrotbane`

A3) `SirCarrotbanePolicy`

Q4) Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?

A4) `ListAllMyBuckets`

Q5) What are the contents of the cloud_password.txt file?

```
ubuntu@tryhackme:~$ aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt
{
    "AcceptRanges": "bytes",
    "LastModified": "2025-12-30T08:18:06+00:00",
    "ContentLength": 29,
    "ETag": "\"c63e1474bf79a91ef95a1e6c8305a304\"",
    "ContentType": "application/octet-stream",
    "Metadata": {}
}
ubuntu@tryhackme:~$ cat cloud_password.txt 
THM{more_like_sir_cloudbane}
```

A5) `THM{more_like_sir_cloudbane}`
