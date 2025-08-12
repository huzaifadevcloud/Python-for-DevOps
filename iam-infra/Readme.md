# IAM User, Policy, and Group Management

This documentation outlines the process for managing IAM users, policies, and groups in AWS. The setup covers:
- Creating and managing IAM users
- Creating and attaching policies
- Managing groups for Developers and DevOps teams
- Listing and deleting IAM resources

---

## 1. **User Management**

### **Create IAM User**
- Create an IAM user with:
  - Username
  - Login password
  - Access key & secret key
- Enable programmatic and console access.

### **List IAM Users**
- Retrieve and display a list of all IAM users in the AWS account.

### **Delete IAM User**
- Steps:
  1. Delete login profile (console password)
  2. Delete all access keys & secret keys
  3. Detach any attached policies
  4. Remove user from groups
  5. Delete the IAM user

---

## 2. **Policy Management**

### **Create Developer Policy**
- Create a JSON policy that grants the required permissions for Developer tasks.
- Save it with a descriptive name, e.g., `DeveloperPolicy`.

### **Create DevOps Policy**
- Create a JSON policy that grants the required permissions for DevOps tasks.
- Save it with a descriptive name, e.g., `DevOpsPolicy`.

### **List Policies**
- Retrieve and display all available policies in the AWS account.

---

## 3. **Group Management**

### **Create Groups**
- Create two groups:
  - `Developers`
  - `DevOps`

### **Attach Policies to Groups**
- Attach `DeveloperPolicy` to the `Developers` group.
- Attach `DevOpsPolicy` to the `DevOps` group.

---

## 4. **Workflow Summary**

1. **User Management**
   - Create user → Assign credentials → Add to group
   - List users
   - Delete user (remove access keys, policies, groups)

2. **Policy Management**
   - Create Developer policy
   - Create DevOps policy
   - List policies

3. **Group Management**
   - Create groups
   - Attach policies to groups
   - Assign users to groups

---

## 5. **Best Practices**
- Use least-privilege permissions.
- Rotate access keys regularly.
- Avoid using root account for daily operations.
- Enable MFA for console login.
