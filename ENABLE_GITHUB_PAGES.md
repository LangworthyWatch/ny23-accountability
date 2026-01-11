# Enable GitHub Pages - Fix 404 Error

Your site is returning 404 because GitHub Pages hasn't been enabled yet.

## Steps to Enable

1. **Go to your repository settings:**
   - Visit: https://github.com/LangworthyWatch/ny23-accountability/settings/pages
   - (Or: Repository → Settings → Pages in left sidebar)

2. **Configure Source:**
   - Under "Build and deployment"
   - **Source:** Select "GitHub Actions" (NOT "Deploy from a branch")
   - This tells GitHub to use the `.github/workflows/hugo.yml` file

3. **Custom Domain:**
   - Under "Custom domain"
   - Enter: `langworthywatch.org`
   - Click "Save"
   - Wait for DNS check to complete (may show "DNS check in progress")

4. **HTTPS:**
   - Once DNS check passes, check "Enforce HTTPS"

## What Should Happen

Once you select "GitHub Actions" as the source:
1. GitHub will automatically run the Hugo workflow
2. It will build your site from the `main` branch
3. Deploy it to `langworthywatch.org`
4. Should be live within 1-2 minutes

## Current Status

✅ DNS configured correctly (A records point to GitHub Pages IPs)
✅ CNAME file in place
✅ Hugo workflow file committed
✅ All content committed and pushed
❌ GitHub Pages not enabled yet ← **This is the issue**

## After You Enable It

The workflow will automatically run whenever you push to `main`, so all your fact-check entries will appear on the live site.

## Verify It Worked

After enabling GitHub Actions as the source, you can check:
1. Go to: https://github.com/LangworthyWatch/ny23-accountability/actions
2. You should see a workflow run starting
3. Wait for it to complete (green checkmark)
4. Visit https://langworthywatch.org - should work!

---

**Note:** You must be logged into the LangworthyWatch GitHub account to access the repository settings.
