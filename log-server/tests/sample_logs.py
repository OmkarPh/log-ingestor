sample_logs = [
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-1234",
    "timestamp": "2022-12-08T00:53:41Z",
    "traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
      "parentResourceId": "server-0987",
      "databaseType": "MySQL"
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-5678",
    "timestamp": "2022-10-27T10:13:31Z",
    "traceId": "def-uvw-456",
    "spanId": "span-789",
    "commit": "7a91bc3",
    "metadata": {
      "parentResourceId": "server-1234",
      "authType": "basic",
      "username": "john_doe"
    }
  },
  {
    "level": "warning",
    "message": "Disk space running low",
    "resourceId": "server-9876",
    "timestamp": "2021-05-11T00:06:30Z",
    "traceId": "ghi-123-jkl",
    "spanId": "span-987",
    "commit": "2c0e5a1",
    "metadata": {
      "parentResourceId": "server-5432",
      "diskDrive": "/dev/sda1"
    }
  },
  {
    "level": "error",
    "message": "Failed to send email",
    "resourceId": "email-2345",
    "timestamp": "2022-03-02T10:56:01Z",
    "traceId": "mno-pqr-789",
    "spanId": "span-654",
    "commit": "8b79ef0",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "confirmation",
      "recipient": "admin@example.com"
    }
  },
  {
    "level": "info",
    "message": "Connected to the database",
    "resourceId": "database-6789",
    "timestamp": "2021-08-15T00:07:29Z",
    "traceId": "stu-vwx-987",
    "spanId": "span-321",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "PostgreSQL",
      "connectionId": "conn-456"
    }
  },
  {
    "level": "error",
    "message": "User authentication failed",
    "resourceId": "user-3456",
    "timestamp": "2021-10-23T17:25:39Z",
    "traceId": "yza-bcd-234",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-5432",
      "authType": "oauth",
      "username": "jane_doe"
    }
  },
  {
    "level": "info",
    "message": "Bulk email sent successfully",
    "resourceId": "bulk-email-1234",
    "timestamp": "2022-02-24T02:43:49Z",
    "traceId": "efg-hij-345",
    "spanId": "span-890",
    "commit": "9c8b7a6",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "newsletter",
      "recipients": [
        "user1@example.com",
        "user2@example.com"
      ]
    }
  },
  {
    "level": "warning",
    "message": "System overheating",
    "resourceId": "server-2345",
    "timestamp": "2022-10-28T16:13:19Z",
    "traceId": "klm-nop-678",
    "spanId": "span-123",
    "commit": "4e3d2f1",
    "metadata": {
      "parentResourceId": "server-1234",
      "temperature": "80\u00b0C"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to external API",
    "resourceId": "api-5678",
    "timestamp": "2021-04-25T03:07:47Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-234",
    "commit": "6a5b4c3",
    "metadata": {
      "parentResourceId": "server-5432",
      "apiName": "third-party-api"
    }
  },
  {
    "level": "info",
    "message": "User account created",
    "resourceId": "user-7890",
    "timestamp": "2023-01-29T00:32:18Z",
    "traceId": "vwx-yza-345",
    "spanId": "span-678",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "accountType": "premium"
    }
  },
  {
    "level": "error",
    "message": "Database connection lost",
    "resourceId": "database-12345",
    "timestamp": "2023-12-02T01:23:35Z",
    "traceId": "bcd-efg-567",
    "spanId": "span-901",
    "commit": "8a9b0c1",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "MongoDB",
      "connectionId": "conn-789"
    }
  },
  {
    "level": "info",
    "message": "Email marked as spam",
    "resourceId": "email-67890",
    "timestamp": "2022-06-07T03:09:26Z",
    "traceId": "stu-vwx-234",
    "spanId": "span-567",
    "commit": "3b4c5d6",
    "metadata": {
      "parentResourceId": "server-5432",
      "emailType": "marketing",
      "recipient": "user3@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Disk space critically low",
    "resourceId": "server-12345",
    "timestamp": "2021-10-04T22:33:53Z",
    "traceId": "yza-bcd-890",
    "spanId": "span-901",
    "commit": "2d3e4f5",
    "metadata": {
      "parentResourceId": "server-9876",
      "diskDrive": "/dev/sdb1"
    }
  },
  {
    "level": "info",
    "message": "User profile updated",
    "resourceId": "user-12345",
    "timestamp": "2021-12-07T06:12:21Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "updateType": "preferences"
    }
  },
  {
    "level": "error",
    "message": "Failed to process payment",
    "resourceId": "payment-67890",
    "timestamp": "2022-04-11T22:04:02Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-5432",
      "paymentMethod": "credit_card"
    }
  },
  {
    "level": "info",
    "message": "Database record deleted",
    "resourceId": "database-23456",
    "timestamp": "2023-08-15T21:27:09Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "databaseType": "SQLite",
      "recordId": "rec-123"
    }
  },
  {
    "level": "error",
    "message": "User account locked",
    "resourceId": "user-78901",
    "timestamp": "2022-01-01T05:33:48Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "accountType": "standard"
    }
  },
  {
    "level": "info",
    "message": "Email bounced back",
    "resourceId": "email-23456",
    "timestamp": "2022-02-28T18:21:26Z",
    "traceId": "bcd-efg-345",
    "spanId": "span-901",
    "commit": "2d3e4f5",
    "metadata": {
      "parentResourceId": "server-5432",
      "emailType": "notification",
      "recipient": "user4@example.com"
    }
  },
  {
    "level": "warning",
    "message": "System reboot required",
    "resourceId": "server-123456",
    "timestamp": "2022-02-15T14:01:09Z",
    "traceId": "klm-nop-678",
    "spanId": "span-234",
    "commit": "6a5b4c3",
    "metadata": {
      "parentResourceId": "server-9876",
      "uptime": "30 days"
    }
  },
  {
    "level": "info",
    "message": "User account deactivated",
    "resourceId": "user-34567",
    "timestamp": "2023-10-01T17:12:58Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "8a9b0c1",
    "metadata": {
      "parentResourceId": "server-1234",
      "accountType": "admin"
    }
  },
  {
    "level": "error",
    "message": "Failed to update software",
    "resourceId": "software-67890",
    "timestamp": "2021-01-14T12:06:55Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "softwareType": "web_server"
    }
  },
  {
    "level": "info",
    "message": "Database backup completed",
    "resourceId": "backup-12345",
    "timestamp": "2021-12-26T01:42:57Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "backupType": "full"
    }
  },
  {
    "level": "warning",
    "message": "Insufficient memory available",
    "resourceId": "server-67890",
    "timestamp": "2022-06-27T10:34:39Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-1234",
      "memoryUsage": "90%"
    }
  },
  {
    "level": "error",
    "message": "User not found",
    "resourceId": "user-123456",
    "timestamp": "2022-05-04T06:40:48Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "searchQuery": "user123"
    }
  },
  {
    "level": "info",
    "message": "Email delivery delayed",
    "resourceId": "email-234567",
    "timestamp": "2021-03-23T09:14:42Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "notification",
      "recipient": "user5@example.com"
    }
  },
  {
    "level": "error",
    "message": "Failed to update configuration",
    "resourceId": "config-345678",
    "timestamp": "2021-04-27T12:04:16Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "configType": "security"
    }
  },
  {
    "level": "info",
    "message": "Database query executed",
    "resourceId": "database-456789",
    "timestamp": "2023-09-03T14:07:03Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "queryType": "SELECT",
      "tableName": "users"
    }
  },
  {
    "level": "warning",
    "message": "System clock out of sync",
    "resourceId": "server-789012",
    "timestamp": "2021-08-01T01:24:10Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "ntpServer": "time.example.com"
    }
  },
  {
    "level": "error",
    "message": "User permission denied",
    "resourceId": "user-234567",
    "timestamp": "2023-03-24T12:29:11Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "permissionType": "write"
    }
  },
  {
    "level": "info",
    "message": "Email opened by recipient",
    "resourceId": "email-345678",
    "timestamp": "2022-03-24T06:44:03Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "marketing",
      "recipient": "user6@example.com"
    }
  },
  {
    "level": "error",
    "message": "Failed to start service",
    "resourceId": "service-456789",
    "timestamp": "2023-04-17T07:44:21Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "serviceName": "web_app"
    }
  },
  {
    "level": "info",
    "message": "Database index created",
    "resourceId": "database-567890",
    "timestamp": "2021-07-06T13:50:37Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "indexName": "idx_users_email"
    }
  },
  {
    "level": "warning",
    "message": "Unexpected server load spike",
    "resourceId": "server-7890123",
    "timestamp": "2021-06-09T11:16:26Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "loadPercentage": "90%"
    }
  },
  {
    "level": "error",
    "message": "User account compromised",
    "resourceId": "user-2345678",
    "timestamp": "2022-11-06T17:49:09Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-5432",
      "securityEvent": "account_compromise"
    }
  },
  {
    "level": "info",
    "message": "Email attachment downloaded",
    "resourceId": "email-3456789",
    "timestamp": "2022-02-12T12:24:43Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "notification",
      "recipient": "user7@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Service degradation detected",
    "resourceId": "service-4567890",
    "timestamp": "2022-03-25T20:57:57Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "api_gateway"
    }
  },
  {
    "level": "error",
    "message": "Database record not found",
    "resourceId": "database-5678901",
    "timestamp": "2022-05-28T10:48:14Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "databaseType": "MongoDB",
      "recordId": "rec-456"
    }
  },
  {
    "level": "info",
    "message": "User account reactivated",
    "resourceId": "user-6789012",
    "timestamp": "2021-01-15T05:29:02Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "accountType": "standard"
    }
  },
  {
    "level": "warning",
    "message": "System memory leak detected",
    "resourceId": "server-7890123",
    "timestamp": "2022-01-11T17:19:39Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "memoryLeakThreshold": "80%"
    }
  },
  {
    "level": "error",
    "message": "User data breach",
    "resourceId": "user-23456789",
    "timestamp": "2021-01-06T10:26:37Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "securityEvent": "data_breach"
    }
  },
  {
    "level": "info",
    "message": "Email marked as important",
    "resourceId": "email-34567890",
    "timestamp": "2022-05-14T18:55:32Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "notification",
      "recipient": "user8@example.com"
    }
  },
  {
    "level": "error",
    "message": "Failed to update firmware",
    "resourceId": "firmware-45678901",
    "timestamp": "2023-05-04T20:51:43Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "firmwareType": "router"
    }
  },
  {
    "level": "info",
    "message": "Database table created",
    "resourceId": "database-56789012",
    "timestamp": "2023-11-21T18:28:04Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "databaseType": "SQLite",
      "tableName": "products"
    }
  },
  {
    "level": "warning",
    "message": "Unexpected power outage",
    "resourceId": "server-78901234",
    "timestamp": "2022-04-26T02:02:03Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "powerSource": "UPS"
    }
  },
  {
    "level": "error",
    "message": "User account deleted",
    "resourceId": "user-234567890",
    "timestamp": "2023-01-03T16:30:47Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "accountType": "admin"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-1234",
    "timestamp": "2021-11-20T20:52:31Z",
    "traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
      "parentResourceId": "server-0987",
      "databaseType": "MySQL"
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-5678",
    "timestamp": "2023-03-17T20:01:56Z",
    "traceId": "def-uvw-456",
    "spanId": "span-789",
    "commit": "7a91bc3",
    "metadata": {
      "parentResourceId": "server-1234",
      "authType": "basic",
      "username": "john_doe"
    }
  },
  {
    "level": "warning",
    "message": "Disk space running low",
    "resourceId": "server-9876",
    "timestamp": "2023-09-10T23:20:04Z",
    "traceId": "ghi-123-jkl",
    "spanId": "span-987",
    "commit": "2c0e5a1",
    "metadata": {
      "parentResourceId": "server-5432",
      "diskDrive": "/dev/sda1"
    }
  },
  {
    "level": "error",
    "message": "Failed to send email",
    "resourceId": "email-2345",
    "timestamp": "2023-09-15T11:23:08Z",
    "traceId": "mno-pqr-789",
    "spanId": "span-654",
    "commit": "8b79ef0",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "confirmation",
      "recipient": "admin@example.com"
    }
  },
  {
    "level": "info",
    "message": "Connected to the database",
    "resourceId": "database-6789",
    "timestamp": "2021-06-04T11:05:26Z",
    "traceId": "stu-vwx-987",
    "spanId": "span-321",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "PostgreSQL",
      "connectionId": "conn-456"
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-8901",
    "timestamp": "2021-12-19T12:13:07Z",
    "traceId": "yza-bcd-234",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-9876",
      "authType": "oauth",
      "username": "jane_doe"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-2345",
    "timestamp": "2022-05-08T09:09:36Z",
    "traceId": "klm-nop-678",
    "spanId": "span-890",
    "commit": "9c8b7a6",
    "metadata": {
      "parentResourceId": "server-3456",
      "databaseType": "MongoDB"
    }
  },
  {
    "level": "info",
    "message": "Bulk email sent successfully",
    "resourceId": "bulk-email-1234",
    "timestamp": "2023-08-13T13:53:37Z",
    "traceId": "efg-hij-345",
    "spanId": "span-123",
    "commit": "4e3d2f1",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "newsletter",
      "recipients": [
        "user1@example.com",
        "user2@example.com"
      ]
    }
  },
  {
    "level": "error",
    "message": "Failed to send bulk email",
    "resourceId": "bulk-email-5678",
    "timestamp": "2023-04-01T07:36:49Z",
    "traceId": "opq-rst-901",
    "spanId": "span-234",
    "commit": "6f7g8h9",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "marketing",
      "recipients": [
        "user3@example.com",
        "user4@example.com"
      ]
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-6789",
    "timestamp": "2023-02-23T18:56:23Z",
    "traceId": "uvw-xyz-567",
    "spanId": "span-890",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-1234",
      "authType": "api-key",
      "username": "api_user"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-4567",
    "timestamp": "2021-08-15T07:54:27Z",
    "traceId": "yza-bcd-234",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-3456",
      "databaseType": "SQLite"
    }
  },
  {
    "level": "warning",
    "message": "Disk space running low",
    "resourceId": "server-8901",
    "timestamp": "2023-11-13T02:33:36Z",
    "traceId": "klm-nop-678",
    "spanId": "span-890",
    "commit": "9c8b7a6",
    "metadata": {
      "parentResourceId": "server-5432",
      "diskDrive": "/dev/sdb1"
    }
  },
  {
    "level": "info",
    "message": "Connected to the database",
    "resourceId": "database-12345",
    "timestamp": "2023-12-05T21:36:53Z",
    "traceId": "efg-hij-345",
    "spanId": "span-123",
    "commit": "4e3d2f1",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "Oracle",
      "connectionId": "conn-789"
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-12345",
    "timestamp": "2021-07-20T19:50:38Z",
    "traceId": "opq-rst-901",
    "spanId": "span-234",
    "commit": "6f7g8h9",
    "metadata": {
      "parentResourceId": "server-9876",
      "authType": "biometric",
      "username": "fingerprint_user"
    }
  },
  {
    "level": "error",
    "message": "Failed to send email",
    "resourceId": "email-78901",
    "timestamp": "2023-05-28T02:05:10Z",
    "traceId": "uvw-xyz-567",
    "spanId": "span-890",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "transactional",
      "recipient": "customer@example.com"
    }
  },
  {
    "level": "info",
    "message": "Connected to the database",
    "resourceId": "database-67890",
    "timestamp": "2023-03-02T23:21:53Z",
    "traceId": "klm-nop-678",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "MongoDB",
      "connectionId": "conn-123"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-56789",
    "timestamp": "2022-04-28T15:24:38Z",
    "traceId": "opq-rst-901",
    "spanId": "span-234",
    "commit": "6f7g8h9",
    "metadata": {
      "parentResourceId": "server-3456",
      "databaseType": "Cassandra"
    }
  },
  {
    "level": "warning",
    "message": "Disk space running low",
    "resourceId": "server-123456",
    "timestamp": "2023-04-17T11:32:41Z",
    "traceId": "uvw-xyz-567",
    "spanId": "span-890",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-5432",
      "diskDrive": "/dev/sdc1"
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-67890",
    "timestamp": "2021-05-03T14:02:41Z",
    "traceId": "efg-hij-345",
    "spanId": "span-123",
    "commit": "4e3d2f1",
    "metadata": {
      "parentResourceId": "server-1234",
      "authType": "jwt",
      "username": "jwt_user"
    }
  },
  {
    "level": "info",
    "message": "Bulk email sent successfully",
    "resourceId": "bulk-email-12345",
    "timestamp": "2023-01-14T19:35:42Z",
    "traceId": "klm-nop-678",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "promotion",
      "recipients": [
        "user5@example.com",
        "user6@example.com"
      ]
    }
  },
  {
    "level": "error",
    "message": "Failed to send bulk email",
    "resourceId": "bulk-email-67890",
    "timestamp": "2022-10-16T17:45:49Z",
    "traceId": "opq-rst-901",
    "spanId": "span-234",
    "commit": "6f7g8h9",
    "metadata": {
      "parentResourceId": "server-9876",
      "emailType": "promotion",
      "recipients": [
        "user7@example.com",
        "user8@example.com"
      ]
    }
  },
  {
    "level": "info",
    "message": "User authentication successful",
    "resourceId": "user-123456",
    "timestamp": "2021-11-04T17:45:18Z",
    "traceId": "uvw-xyz-567",
    "spanId": "span-890",
    "commit": "1a2b3c4",
    "metadata": {
      "parentResourceId": "server-1234",
      "authType": "saml",
      "username": "saml_user"
    }
  },
  {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-78901",
    "timestamp": "2023-10-27T05:37:48Z",
    "traceId": "efg-hij-345",
    "spanId": "span-123",
    "commit": "4e3d2f1",
    "metadata": {
      "parentResourceId": "server-3456",
      "databaseType": "Redis"
    }
  },
  {
    "level": "warning",
    "message": "Disk space running low",
    "resourceId": "server-234567",
    "timestamp": "2021-06-27T06:49:04Z",
    "traceId": "klm-nop-678",
    "spanId": "span-567",
    "commit": "5d6e7f8",
    "metadata": {
      "parentResourceId": "server-5432",
      "diskDrive": "/dev/sdd1"
    }
  },
  {
    "level": "info",
    "message": "Connected to the database",
    "resourceId": "database-789012",
    "timestamp": "2023-12-02T22:50:15Z",
    "traceId": "opq-rst-901",
    "spanId": "span-234",
    "commit": "6f7g8h9",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "SQLite",
      "connectionId": "conn-567"
    }
  },
  {
    "level": "info",
    "message": "User profile picture updated",
    "resourceId": "user-12345",
    "timestamp": "2021-03-15T07:44:45Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "updateType": "profile_picture"
    }
  },
  {
    "level": "warning",
    "message": "SSL certificate expiration",
    "resourceId": "server-23456",
    "timestamp": "2021-07-26T14:57:43Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "certificateName": "example.com"
    }
  },
  {
    "level": "error",
    "message": "Payment gateway timeout",
    "resourceId": "payment-345678",
    "timestamp": "2021-07-23T04:58:29Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "paymentMethod": "paypal"
    }
  },
  {
    "level": "info",
    "message": "New user registered",
    "resourceId": "user-456789",
    "timestamp": "2021-10-25T09:37:38Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-1234",
      "registrationSource": "web"
    }
  },
  {
    "level": "warning",
    "message": "Server disk space cleanup",
    "resourceId": "server-567890",
    "timestamp": "2022-07-22T22:39:18Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "cleanupThreshold": "85%"
    }
  },
  {
    "level": "error",
    "message": "Authentication token expired",
    "resourceId": "user-678901",
    "timestamp": "2021-01-03T12:32:46Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "authType": "jwt"
    }
  },
  {
    "level": "info",
    "message": "Database schema updated",
    "resourceId": "database-789012",
    "timestamp": "2023-10-28T08:54:53Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "MySQL",
      "schemaVersion": "2.0"
    }
  },
  {
    "level": "warning",
    "message": "Service outage reported",
    "resourceId": "service-890123",
    "timestamp": "2023-01-21T20:41:01Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "notification_service"
    }
  },
  {
    "level": "error",
    "message": "Failed to process order",
    "resourceId": "order-123456",
    "timestamp": "2023-06-27T13:49:54Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "orderType": "online_purchase"
    }
  },
  {
    "level": "info",
    "message": "User account upgraded",
    "resourceId": "user-234567",
    "timestamp": "2021-04-08T07:33:34Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "accountType": "premium"
    }
  },
  {
    "level": "warning",
    "message": "High network latency detected",
    "resourceId": "server-345678",
    "timestamp": "2023-04-05T18:32:51Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "networkLocation": "datacenter-1"
    }
  },
  {
    "level": "error",
    "message": "File upload failed",
    "resourceId": "file-456789",
    "timestamp": "2021-02-22T07:57:48Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "uploadType": "image"
    }
  },
  {
    "level": "info",
    "message": "Database index rebuild",
    "resourceId": "database-567890",
    "timestamp": "2021-06-19T22:22:55Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "indexName": "idx_products_name"
    }
  },
  {
    "level": "warning",
    "message": "Service version update available",
    "resourceId": "service-678901",
    "timestamp": "2021-09-10T06:55:39Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "authentication"
    }
  },
  {
    "level": "error",
    "message": "User login failed",
    "resourceId": "user-789012",
    "timestamp": "2022-02-25T10:11:03Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "loginType": "social"
    }
  },
  {
    "level": "info",
    "message": "Email unsubscribe request",
    "resourceId": "email-890123",
    "timestamp": "2022-05-03T15:12:33Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "marketing",
      "recipient": "user9@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server API rate limit exceeded",
    "resourceId": "server-901234",
    "timestamp": "2023-04-27T20:53:24Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "apiName": "user_profile"
    }
  },
  {
    "level": "error",
    "message": "Failed to send push notification",
    "resourceId": "notification-123456",
    "timestamp": "2022-05-22T19:53:16Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "notificationType": "alert"
    }
  },
  {
    "level": "info",
    "message": "Database connection pool expanded",
    "resourceId": "database-234567",
    "timestamp": "2022-06-24T06:44:44Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "poolSize": "50"
    }
  },
  {
    "level": "warning",
    "message": "Unexpected server restart",
    "resourceId": "server-345678",
    "timestamp": "2021-01-10T23:36:53Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "restartCause": "system_update"
    }
  },
  {
    "level": "error",
    "message": "User data modification detected",
    "resourceId": "user-4567890",
    "timestamp": "2023-06-01T23:21:04Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "modificationType": "profile_update"
    }
  },
  {
    "level": "info",
    "message": "Email marked as spam",
    "resourceId": "email-5678901",
    "timestamp": "2022-07-02T22:04:27Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "promotion",
      "recipient": "user10@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server maintenance scheduled",
    "resourceId": "server-6789012",
    "timestamp": "2022-01-28T08:13:33Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "maintenanceWindow": "2 hours"
    }
  },
  {
    "level": "error",
    "message": "Failed to process refund",
    "resourceId": "refund-7890123",
    "timestamp": "2021-01-01T03:29:59Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "refundType": "credit_card"
    }
  },
  {
    "level": "info",
    "message": "User password reset",
    "resourceId": "user-9012345",
    "timestamp": "2022-03-11T15:13:22Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "resetMethod": "email"
    }
  },
  {
    "level": "warning",
    "message": "Network firewall rule modified",
    "resourceId": "firewall-1234567",
    "timestamp": "2021-09-17T11:09:01Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "firewallRuleId": "rule-5678"
    }
  },
  {
    "level": "error",
    "message": "Critical database error",
    "resourceId": "database-2345678",
    "timestamp": "2022-03-29T23:47:45Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "errorType": "deadlock"
    }
  },
  {
    "level": "info",
    "message": "Email sent successfully",
    "resourceId": "email-3456789",
    "timestamp": "2021-07-24T01:23:43Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "notification",
      "recipient": "user11@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server CPU usage spike",
    "resourceId": "server-45678901",
    "timestamp": "2023-03-18T01:40:16Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "cpuUsagePercentage": "95%"
    }
  },
  {
    "level": "error",
    "message": "Failed login attempt",
    "resourceId": "user-56789012",
    "timestamp": "2023-12-24T21:15:06Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "loginType": "password"
    }
  },
  {
    "level": "info",
    "message": "Database backup completed",
    "resourceId": "backup-67890123",
    "timestamp": "2023-06-19T03:05:21Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "backupType": "full"
    }
  },
  {
    "level": "warning",
    "message": "Service API version deprecated",
    "resourceId": "service-78901234",
    "timestamp": "2021-09-12T11:52:02Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "user_management"
    }
  },
  {
    "level": "error",
    "message": "User session expired",
    "resourceId": "user-90123456",
    "timestamp": "2022-10-18T20:11:56Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "sessionType": "web"
    }
  },
  {
    "level": "info",
    "message": "Email bounce detected",
    "resourceId": "email-123456789",
    "timestamp": "2022-04-27T18:39:56Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "marketing",
      "recipient": "user12@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server software update available",
    "resourceId": "server-234567890",
    "timestamp": "2023-08-21T01:11:29Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "updateType": "security_patch"
    }
  },
  {
    "level": "error",
    "message": "Database connection timeout",
    "resourceId": "database-345678901",
    "timestamp": "2023-04-20T06:57:20Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "databaseType": "PostgreSQL"
    }
  },
  {
    "level": "info",
    "message": "User session started",
    "resourceId": "user-456789012",
    "timestamp": "2023-07-18T09:11:16Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "sessionType": "mobile"
    }
  },
  {
    "level": "warning",
    "message": "Service endpoint unreachable",
    "resourceId": "service-567890123",
    "timestamp": "2022-05-04T12:05:31Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "notification_delivery"
    }
  },
  {
    "level": "error",
    "message": "File download failed",
    "resourceId": "file-678901234",
    "timestamp": "2022-09-10T13:55:57Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "downloadType": "document"
    }
  },
  {
    "level": "info",
    "message": "Database query optimization",
    "resourceId": "database-789012345",
    "timestamp": "2021-07-19T04:24:50Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "MongoDB",
      "queryName": "user_profile"
    }
  },
  {
    "level": "warning",
    "message": "Service request rejected",
    "resourceId": "service-901234567",
    "timestamp": "2021-12-29T07:16:03Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "payment_gateway"
    }
  },
  {
    "level": "error",
    "message": "User data deletion",
    "resourceId": "user-1234567890",
    "timestamp": "2021-04-19T17:51:53Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-5432",
      "deleteType": "account"
    }
  },
  {
    "level": "info",
    "message": "Email delivery success",
    "resourceId": "email-2345678901",
    "timestamp": "2021-01-01T14:26:27Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "transactional",
      "recipient": "user13@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server memory leak detected",
    "resourceId": "server-3456789012",
    "timestamp": "2022-05-27T20:21:09Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "leakType": "heap"
    }
  },
  {
    "level": "error",
    "message": "Failed API authentication",
    "resourceId": "api-4567890123",
    "timestamp": "2021-08-20T21:41:45Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "apiName": "user_data"
    }
  },
  {
    "level": "info",
    "message": "Database transaction rollback",
    "resourceId": "database-5678901234",
    "timestamp": "2022-09-20T14:11:10Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "Oracle",
      "transactionId": "txn-789012"
    }
  },
  {
    "level": "warning",
    "message": "Service request timeout",
    "resourceId": "service-6789012345",
    "timestamp": "2021-01-17T01:04:29Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "file_storage"
    }
  },
  {
    "level": "error",
    "message": "User access denied",
    "resourceId": "user-7890123456",
    "timestamp": "2023-09-13T13:35:51Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "accessType": "admin_panel"
    }
  },
  {
    "level": "info",
    "message": "Email attachment added",
    "resourceId": "email-9012345678",
    "timestamp": "2021-04-05T20:46:03Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "newsletter",
      "recipient": "user14@example.com",
      "attachmentType": "image"
    }
  },
  {
    "level": "warning",
    "message": "Server disk failure",
    "resourceId": "server-12345678901",
    "timestamp": "2022-03-20T00:32:20Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "diskId": "disk-1234"
    }
  },
  {
    "level": "error",
    "message": "Failed to process subscription",
    "resourceId": "subscription-23456789012",
    "timestamp": "2021-01-04T00:41:18Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "subscriptionType": "monthly_plan"
    }
  },
  {
    "level": "info",
    "message": "Database record deleted",
    "resourceId": "database-34567890123",
    "timestamp": "2021-05-21T00:53:36Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "databaseType": "SQLite",
      "tableName": "user_profiles",
      "recordId": "user-15"
    }
  },
  {
    "level": "warning",
    "message": "Service downtime scheduled",
    "resourceId": "service-45678901234",
    "timestamp": "2022-08-24T17:41:31Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "downtimeDuration": "4 hours",
      "serviceName": "billing"
    }
  },
  {
    "level": "error",
    "message": "User account locked",
    "resourceId": "user-56789012345",
    "timestamp": "2022-11-06T06:18:26Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "lockReason": "multiple_failed_attempts"
    }
  },
  {
    "level": "info",
    "message": "Email marked as important",
    "resourceId": "email-67890123456",
    "timestamp": "2023-05-04T16:15:14Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "emailType": "inbox",
      "recipient": "user16@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server power outage detected",
    "resourceId": "server-78901234567",
    "timestamp": "2022-02-21T12:51:35Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-9876",
      "outageDuration": "2 hours"
    }
  },
  {
    "level": "error",
    "message": "Failed to process order return",
    "resourceId": "order-89012345678",
    "timestamp": "2023-01-29T09:41:29Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-5432",
      "returnType": "defective_item"
    }
  },
  {
    "level": "info",
    "message": "User profile data retrieved",
    "resourceId": "user-90123456789",
    "timestamp": "2021-12-20T18:16:56Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-1234",
      "retrieveType": "full"
    }
  },
  {
    "level": "warning",
    "message": "Service network outage",
    "resourceId": "service-123456789012",
    "timestamp": "2022-02-02T05:29:26Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-9876",
      "outageLocation": "datacenter-2"
    }
  },
  {
    "level": "error",
    "message": "User data corruption detected",
    "resourceId": "user-23456789012",
    "timestamp": "2023-08-21T18:43:07Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-5432",
      "corruptionType": "file_system"
    }
  },
  {
    "level": "info",
    "message": "Email draft saved",
    "resourceId": "email-34567890123",
    "timestamp": "2023-09-22T19:36:19Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-1234",
      "emailType": "draft",
      "recipient": "user17@example.com"
    }
  },
  {
    "level": "warning",
    "message": "Server API rate limit exceeded",
    "resourceId": "server-45678901234",
    "timestamp": "2021-11-28T20:17:09Z",
    "traceId": "abc-def-345",
    "spanId": "span-678",
    "commit": "6g7h8i9",
    "metadata": {
      "parentResourceId": "server-9876",
      "apiName": "data_fetch"
    }
  },
  {
    "level": "error",
    "message": "Failed to process subscription cancellation",
    "resourceId": "subscription-56789012345",
    "timestamp": "2023-01-13T21:01:13Z",
    "traceId": "jkl-mno-789",
    "spanId": "span-234",
    "commit": "5e6f7a8",
    "metadata": {
      "parentResourceId": "server-5432",
      "cancellationType": "auto_renewal"
    }
  },
  {
    "level": "info",
    "message": "Database index creation",
    "resourceId": "database-67890123456",
    "timestamp": "2022-06-06T12:21:22Z",
    "traceId": "pqr-stu-901",
    "spanId": "span-567",
    "commit": "9a8b7c6",
    "metadata": {
      "parentResourceId": "server-1234",
      "indexName": "idx_logs_timestamp"
    }
  },
  {
    "level": "warning",
    "message": "Service version update available",
    "resourceId": "service-78901234567",
    "timestamp": "2022-09-08T00:04:15Z",
    "traceId": "vwx-yza-234",
    "spanId": "span-890",
    "commit": "1d2e3f4",
    "metadata": {
      "parentResourceId": "server-9876",
      "serviceName": "authentication"
    }
  }
]

# print("Sample logs:", len(sample_logs))