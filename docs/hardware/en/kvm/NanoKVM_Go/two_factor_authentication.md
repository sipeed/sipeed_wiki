---
title: Two-Factor Authentication
keywords: NanoKVM Go, two-factor authentication, 2FA, authenticator, recovery codes
---

## Configure Two-Factor Authentication

Two-factor authentication (2FA) adds an authentication code to password-based sign-in.

1. Install Google Authenticator or Microsoft Authenticator on your phone. The steps below use Google Authenticator.

2. Sign in to NanoKVM Go and click the Settings icon in the floating toolbar.

![Open NanoKVM Go settings](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-settings-entry.webp)

3. Select `Account`, then click `Enable` next to `Two-factor authentication`.

![Enable two-factor authentication on NanoKVM Go](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-enable-en.webp)

4. Enter your current password, then click `Enable`.

![Confirm the current password](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-password-confirmation-en.webp)

5. Scan the QR code with the authenticator app, or enter the setup key manually.

![Scan the QR code or use the setup key](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-qr-code-and-secret-key-en.webp)

![Add a NanoKVM Go account in the authenticator app](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-authenticator-add-account-en.webp)

6. Enter the current code from the authenticator app, then click `Verify and enable`.

![NanoKVM Go authentication code in the authenticator app](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-authenticator-code.webp)

![Verify and enable two-factor authentication](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-verification-code-submit-en.webp)

7. After 2FA is enabled, all sessions are logged out. Sign in again.

![Two-factor authentication enabled notice](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-enabled-login-notice-en.webp)

8. Enter the current authentication code or a recovery code, then click `Verify`.

![Complete two-factor verification](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-login-verification-en.webp)

## Configure Recovery Codes

Recovery codes are one-time backup codes for signing in when the authenticator app is unavailable. Save them securely when they are generated.

1. In `Settings`, select `Account`, then click `Enable` next to `Recovery codes`.

![Enable recovery codes on NanoKVM Go](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-recovery-code-enable-en.webp)

2. Enter your current password and authentication code, then click `Enable` to generate the recovery codes.

![Confirm recovery code generation](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-recovery-code-password-confirmation-en.webp)

3. Click `Copy` or `Download` before leaving the page, then click `Done`.

![Save the generated recovery codes](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-recovery-codes-en.webp)

4. If the recovery codes are lost or may have been exposed, click `Update` and save the new set immediately.

![Update the recovery codes](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-recovery-codes-update-en.webp)

## Advanced 2FA Protection

Advanced 2FA Protection requires a second-factor code for selected sensitive operations.

1. In `Settings`, select `Account`, then expand `Advanced 2FA Protection`.

![Open Advanced 2FA Protection](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-advanced-protection-entry-en.webp)

2. Enable protection for the operations that should require a second factor. Available options include `Direct web login`, `Web Terminal`, `SSH`, `Tailscale`, `MCP`, `Target machine power`, `NanoKVM restart`, `Script operations`, `Screen Timelapse`, and `Delete image`.

![Select Advanced 2FA Protection options](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-advanced-protection-options-en.webp)

3. A blue toggle indicates that protection is enabled; a gray toggle indicates that it is disabled. When enabled, the selected operation requires a verification code before it can proceed.

## Disable Two-Factor Authentication

1. In `Settings`, select `Account`, then click `Disable` next to `Two-factor authentication`.

![Disable two-factor authentication on NanoKVM Go](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-disable-en.webp)

2. Enter your current password and either an authenticator-generated code or an unused recovery code, then click `Disable`.

![Confirm disabling two-factor authentication](./../../../assets/NanoKVM/go/two_factor_authentication/nanokvm-go-2fa-disable-confirmation-en.webp)
