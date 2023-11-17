sample_logs = [
    {
        "level": "error",
        "message": "Failed to connect to DB",
        "resourceId": "server-1234",
        "timestamp": "2023-09-15T08:00:00Z",
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
        "timestamp": "2023-09-15T08:15:00Z",
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
        "timestamp": "2023-09-15T08:30:00Z",
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
        "timestamp": "2023-09-15T08:45:00Z",
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
        "timestamp": "2023-09-15T09:00:00Z",
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
        "timestamp": "2023-09-15T09:15:00Z",
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
        "timestamp": "2023-09-15T09:30:00Z",
        "traceId": "efg-hij-345",
        "spanId": "span-890",
        "commit": "9c8b7a6",
        "metadata": {
            "parentResourceId": "server-9876",
            "emailType": "newsletter",
            "recipients": ["user1@example.com", "user2@example.com"]
        }
    },
    {
        "level": "warning",
        "message": "System overheating",
        "resourceId": "server-2345",
        "timestamp": "2023-09-15T09:45:00Z",
        "traceId": "klm-nop-678",
        "spanId": "span-123",
        "commit": "4e3d2f1",
        "metadata": {
            "parentResourceId": "server-1234",
            "temperature": "80°C"
        }
    },
    {
        "level": "error",
        "message": "Failed to connect to external API",
        "resourceId": "api-5678",
        "timestamp": "2023-09-15T10:00:00Z",
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
        "timestamp": "2023-09-15T10:15:00Z",
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
        "timestamp": "2023-09-15T10:30:00Z",
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
        "timestamp": "2023-09-15T10:45:00Z",
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
        "timestamp": "2023-09-15T11:00:00Z",
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
        "timestamp": "2023-09-15T11:15:00Z",
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
        "timestamp": "2023-09-15T11:30:00Z",
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
        "timestamp": "2023-09-15T11:45:00Z",
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
        "timestamp": "2023-09-15T12:00:00Z",
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
        "timestamp": "2023-09-15T12:15:00Z",
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
        "timestamp": "2023-09-15T12:30:00Z",
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
        "timestamp": "2023-09-15T12:45:00Z",
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
        "timestamp": "2023-09-15T13:00:00Z",
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
        "timestamp": "2023-09-15T13:15:00Z",
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
        "timestamp": "2023-09-15T13:30:00Z",
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
        "timestamp": "2023-09-15T13:45:00Z",
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
        "timestamp": "2023-09-15T14:00:00Z",
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
        "timestamp": "2023-09-15T14:15:00Z",
        "traceId": "abc-def-345",
        "spanId": "span-678",
        "commit": "6g7h8i9",
        "metadata": {
            "parentResourceId": "server-1234",
            "configType": "security"
        }
    }, {
        "level": "info",
        "message": "Database query executed",
        "resourceId": "database-456789",
        "timestamp": "2023-09-15T14:30:00Z",
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
        "timestamp": "2023-09-15T14:45:00Z",
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
        "timestamp": "2023-09-15T15:00:00Z",
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
        "timestamp": "2023-09-15T15:15:00Z",
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
        "timestamp": "2023-09-15T15:30:00Z",
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
        "timestamp": "2023-09-15T15:45:00Z",
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
        "timestamp": "2023-09-15T16:00:00Z",
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
        "timestamp": "2023-09-15T16:15:00Z",
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
        "timestamp": "2023-09-15T16:30:00Z",
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
        "timestamp": "2023-09-15T16:45:00Z",
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
        "timestamp": "2023-09-15T17:00:00Z",
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
        "timestamp": "2023-09-15T17:15:00Z",
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
        "timestamp": "2023-09-15T17:30:00Z",
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
        "timestamp": "2023-09-15T17:45:00Z",
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
        "timestamp": "2023-09-15T18:00:00Z",
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
        "timestamp": "2023-09-15T18:15:00Z",
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
        "timestamp": "2023-09-15T18:30:00Z",
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
        "timestamp": "2023-09-15T18:45:00Z",
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
        "timestamp": "2023-09-15T19:00:00Z",
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
        "timestamp": "2023-09-15T08:00:00Z",
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
        "timestamp": "2023-09-15T08:15:00Z",
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
        "timestamp": "2023-09-15T08:30:00Z",
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
        "timestamp": "2023-09-15T08:45:00Z",
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
        "timestamp": "2023-09-15T09:00:00Z",
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
        "timestamp": "2023-09-15T09:15:00Z",
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
        "timestamp": "2023-09-15T09:30:00Z",
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
        "timestamp": "2023-09-15T09:45:00Z",
        "traceId": "efg-hij-345",
        "spanId": "span-123",
        "commit": "4e3d2f1",
        "metadata": {
            "parentResourceId": "server-1234",
            "emailType": "newsletter",
            "recipients": ["user1@example.com", "user2@example.com"]
        }
    },
    {
        "level": "error",
        "message": "Failed to send bulk email",
        "resourceId": "bulk-email-5678",
        "timestamp": "2023-09-15T10:00:00Z",
        "traceId": "opq-rst-901",
        "spanId": "span-234",
        "commit": "6f7g8h9",
        "metadata": {
            "parentResourceId": "server-9876",
            "emailType": "marketing",
            "recipients": ["user3@example.com", "user4@example.com"]
        }
    },
    {
        "level": "info",
        "message": "User authentication successful",
        "resourceId": "user-6789",
        "timestamp": "2023-09-15T10:15:00Z",
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
        "timestamp": "2023-09-15T10:30:00Z",
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
        "timestamp": "2023-09-15T10:45:00Z",
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
        "timestamp": "2023-09-15T11:00:00Z",
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
        "timestamp": "2023-09-15T11:15:00Z",
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
        "timestamp": "2023-09-15T11:30:00Z",
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
        "timestamp": "2023-09-15T11:45:00Z",
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
        "timestamp": "2023-09-15T12:00:00Z",
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
        "timestamp": "2023-09-15T12:15:00Z",
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
        "timestamp": "2023-09-15T12:30:00Z",
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
        "timestamp": "2023-09-15T12:45:00Z",
        "traceId": "klm-nop-678",
        "spanId": "span-567",
        "commit": "5d6e7f8",
        "metadata": {
            "parentResourceId": "server-1234",
            "emailType": "promotion",
            "recipients": ["user5@example.com", "user6@example.com"]
        }
    },
    {
        "level": "error",
        "message": "Failed to send bulk email",
        "resourceId": "bulk-email-67890",
        "timestamp": "2023-09-15T13:00:00Z",
        "traceId": "opq-rst-901",
        "spanId": "span-234",
        "commit": "6f7g8h9",
        "metadata": {
            "parentResourceId": "server-9876",
            "emailType": "promotion",
            "recipients": ["user7@example.com", "user8@example.com"]
        }
    },
    {
        "level": "info",
        "message": "User authentication successful",
        "resourceId": "user-123456",
        "timestamp": "2023-09-15T13:15:00Z",
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
        "timestamp": "2023-09-15T13:30:00Z",
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
        "timestamp": "2023-09-15T13:45:00Z",
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
        "timestamp": "2023-09-15T14:00:00Z",
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
        "timestamp": "2023-09-16T08:00:00Z",
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
        "timestamp": "2023-09-16T08:15:00Z",
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
        "timestamp": "2023-09-16T08:30:00Z",
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
        "timestamp": "2023-09-16T08:45:00Z",
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
        "timestamp": "2023-09-16T09:00:00Z",
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
        "timestamp": "2023-09-16T09:15:00Z",
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
        "timestamp": "2023-09-16T09:30:00Z",
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
        "timestamp": "2023-09-16T09:45:00Z",
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
        "timestamp": "2023-09-16T10:00:00Z",
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
        "timestamp": "2023-09-16T10:15:00Z",
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
        "timestamp": "2023-09-16T10:30:00Z",
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
        "timestamp": "2023-09-16T10:45:00Z",
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
        "timestamp": "2023-09-16T11:00:00Z",
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
        "timestamp": "2023-09-16T11:15:00Z",
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
        "timestamp": "2023-09-16T11:30:00Z",
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
        "timestamp": "2023-09-16T11:45:00Z",
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
        "timestamp": "2023-09-16T12:00:00Z",
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
        "timestamp": "2023-09-16T12:15:00Z",
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
        "timestamp": "2023-09-16T12:30:00Z",
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
        "timestamp": "2023-09-16T12:45:00Z",
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
        "timestamp": "2023-09-16T13:00:00Z",
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
        "timestamp": "2023-09-16T13:15:00Z",
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
        "timestamp": "2023-09-16T13:30:00Z",
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
        "timestamp": "2023-09-16T13:45:00Z",
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
        "timestamp": "2023-09-16T14:00:00Z",
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
        "timestamp": "2023-09-16T14:15:00Z",
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
        "timestamp": "2023-09-16T14:30:00Z",
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
        "timestamp": "2023-09-16T14:45:00Z",
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
        "timestamp": "2023-09-16T15:00:00Z",
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
        "timestamp": "2023-09-16T15:15:00Z",
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
        "timestamp": "2023-09-16T15:30:00Z",
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
        "timestamp": "2023-09-16T15:45:00Z",
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
        "timestamp": "2023-09-16T16:00:00Z",
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
        "timestamp": "2023-09-16T16:15:00Z",
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
        "timestamp": "2023-09-16T16:30:00Z",
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
        "timestamp": "2023-09-16T16:45:00Z",
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
        "timestamp": "2023-09-16T17:00:00Z",
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
        "timestamp": "2023-09-16T17:15:00Z",
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
        "timestamp": "2023-09-16T17:30:00Z",
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
        "timestamp": "2023-09-16T17:45:00Z",
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
        "timestamp": "2023-09-16T18:00:00Z",
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
        "timestamp": "2023-09-16T18:15:00Z",
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
        "timestamp": "2023-09-16T18:30:00Z",
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
        "timestamp": "2023-09-16T18:45:00Z",
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
        "timestamp": "2023-09-16T19:00:00Z",
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
        "timestamp": "2023-09-16T19:15:00Z",
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
        "timestamp": "2023-09-16T19:30:00Z",
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
        "timestamp": "2023-09-16T19:45:00Z",
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
        "timestamp": "2023-09-16T20:00:00Z",
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
        "timestamp": "2023-09-16T20:15:00Z",
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
        "timestamp": "2023-09-16T20:30:00Z",
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
        "timestamp": "2023-09-16T20:45:00Z",
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
        "timestamp": "2023-09-16T21:00:00Z",
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
        "timestamp": "2023-09-16T21:15:00Z",
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
        "timestamp": "2023-09-16T21:30:00Z",
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
        "timestamp": "2023-09-16T21:45:00Z",
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
        "timestamp": "2023-09-16T22:00:00Z",
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
        "timestamp": "2023-09-16T22:15:00Z",
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
        "timestamp": "2023-09-16T22:30:00Z",
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
        "timestamp": "2023-09-16T22:45:00Z",
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
        "timestamp": "2023-09-16T23:00:00Z",
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
        "timestamp": "2023-09-16T23:15:00Z",
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
        "timestamp": "2023-09-16T23:30:00Z",
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
        "timestamp": "2023-09-16T23:45:00Z",
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
        "timestamp": "2023-09-17T00:00:00Z",
        "traceId": "vwx-yza-234",
        "spanId": "span-890",
        "commit": "1d2e3f4",
        "metadata": {
            "parentResourceId": "server-9876",
            "serviceName": "authentication"
        }
    }

]

print("Sample logs:", len(sample_logs))