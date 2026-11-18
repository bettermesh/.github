# BetterMesh brand assets

This public directory owns the BetterMesh brand masters. The app and helper repositories carry byte-identical copies in `assets/brand` so their READMEs work without cross-repository image requests.

- `bettermesh-logo.svg` is the transparent horizontal logo for light backgrounds.
- `bettermesh-logo-dark.svg` is the transparent horizontal logo for dark backgrounds.
- `bettermesh-icon.svg` is the square master icon.
- `bettermesh-icon.png` is the 1024 × 1024 sRGB export for the organization avatar.

The logos use outlined lettering and do not depend on fonts. Keep the viewBox, proportions and padding. Use alt text when embedding a meaningful image, or empty alt text beside an equivalent text label. Teal is `#40DEC2`, navy is `#101E2D` and off-white is `#F5F8FC`.

Change the masters here and copy all four files into the app and helper repositories in linked PRs. Do not reference the private app repository from this public profile. The profile's absolute image URLs point at this repository's `main` branch and become available when the asset PR is merged.

## GitHub settings

After merging, an organization owner must upload `bettermesh-icon.png` at <https://github.com/organizations/bettermesh/settings/profile>. Choose **Upload new picture** under the existing avatar. Merging this repository's README does not change the avatar.

For repository social previews, prepare a separate wide image and upload it through each repository's settings. Do not stretch the square icon or use the horizontal wordmark as an avatar.

These are project identity assets. Their presence here does not change the license or visibility of the BetterMesh apps or helper.
