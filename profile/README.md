# BetterMesh

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bettermesh/.github/main/profile/assets/bettermesh-logo-dark.svg">
  <img src="https://raw.githubusercontent.com/bettermesh/.github/main/profile/assets/bettermesh-logo.svg" alt="BetterMesh logo" width="440" height="102">
</picture>

One view of your Wi-Fi network, across the routers and access points you choose.

BetterMesh is a planned phone and desktop app for managing several OpenWrt-based routers as one network. Wired backhaul comes first. Despite the name, the initial target is a multi-access-point network connected by Ethernet, not an 802.11s wireless mesh.

**Status: early development. There is no installable release yet.** The features below describe the design, not software you can use today.

## What we're building

- A network map and client list showing which access point and band each device uses.
- A checkup for overlapping channels, inconsistent Wi-Fi settings and other network problems.
- A readiness report that says what each router supports, including what is unknown or untested.
- Guided fast roaming setup using 802.11r, 802.11k and 802.11v where the hardware and firmware support them.
- Channel planning and client steering, with explanations of the proposed settings.
- A readable diff, backup and automatic rollback for configuration changes.

The first firmware targets are upstream OpenWrt and GL.iNet stock firmware. Support depends on the model, driver and firmware version. Fast roaming between different firmware families needs hardware testing; it is not guaranteed.

## Your network stays yours

BetterMesh is designed to write ordinary router configuration. Removing its helper should leave the network working with those settings.

The planned free tier provides local, read-only monitoring and checkups without an account or calls outside your network. Paid subscriptions will fund configuration features and ongoing firmware compatibility work. A built-in assistant is planned separately, with consent before network data is sent to a hosted service.

AI tools will be able to inspect network state and propose changes, but not apply them. Approval belongs in the app.

## What's open

The BetterMesh Helper, the code that runs on each router, is intended to be public under Apache-2.0 when it has working code. The apps are proprietary.

The helper is designed to record requests in an audit log that the app's credential cannot edit or clear. Auditing and uninstalling will not require a subscription. That log covers requests reaching the router, not what an app does elsewhere on your device.

The app and helper repositories are private during this initial work. This profile is the public starting point.

BetterMesh is an independent project, not affiliated with OpenWrt or GL.iNet.
