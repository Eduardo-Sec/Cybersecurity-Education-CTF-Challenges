3. XSS Vulnerability (Beginner-Friendly)
**Difficulty:** Easy  
**Category:** Web Awareness  

**Objective:** Try different inputs and understand how unsafe code can be reflected on a website.

**Scenario:**
Your school has a comment section that doesn't filter special characters. When you post something, it shows up on the page exactly as you typed it.

**Instructions:**
- Open `xxs_demo.html` in your browser.
- In the comment box, try typing: `<script>FLAG{webpages_need_filters}</script>`
- Post the comment and observe what happens.

**Hint:** You're learning what happens when webpages don't escape dangerous characters.

**Flag Format:** `FLAG{webpages_need_filters}`