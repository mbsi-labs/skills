# The SEO runbook

How a page gets found by people and by AI agents, in order, and how sure we are of each belief. For anyone who ships or markets a page on a new site.

## 1. Which source wins

1. **Google's and Bing's own pages** about their engines come first.
2. **Your own measurements** come next: Search Console, Bing Webmaster, your analytics, your link record. When they disagree with a study, yours are about your site, so they win for your site.
3. **Studies with a method** (Backlinko's 912M posts, Moz and BuzzSumo, Ahrefs' outreach counts) come third.
4. **Vendor academies and university syllabi** come last. A syllabus shows what is taught, not what works. The syllabi we read did not cover how a brand-new site gets found, which is the step that blocks a new site.

## 2. The order of work

### 2.1 Be findable

Google finds pages "when Google extracts a link from a known page to a new page" or "when you submit a list of pages (a sitemap)". A sitemap "can be very helpful if you just launched your site". Bing names four ways in: IndexNow, XML sitemaps, crawlable internal links, and "External links from relevant websites".

1. Every page is in the site's `sitemap.xml`, and robots.txt names the sitemap.
2. The sitemap is submitted in Google Search Console and Bing Webmaster.
3. Every new page is linked from a page that is already indexed: the home page, a hub page or a related guide.
4. After each production deploy, send the changed URLs to IndexNow, or with Bing's URL submission (100 a day per site), and resubmit the sitemap in Search Console.
5. Links from other sites come last in this list, but they matter most for third-party link tools and for pages nobody else points to (2.5).

### 2.2 Check it is stored, not only crawled

1. Google: the URL Inspection tool in Search Console. "URL is unknown to Google" means not stored.
2. Bing: the Webmaster API's GetUrlInfo. A page is stored only when `DocumentSize` is above 0. A `LastCrawledDate` alone means Bing tried, not that it kept the page.
3. Report counts per site: stored, crawled but not stored, unknown.

### 2.3 Wait the stated time, and don't re-request

1. "Google doesn't guarantee that it will crawl, index, or serve your page, even if your page follows the Google Search Essentials."
2. A recrawl "can take anywhere from a few days to a few weeks", and requesting it again "won't get it crawled any faster".
3. A domain with a past (parked or unregistered for years) can take longer. Google's John Mueller: "Sometimes it just takes a lot of time for the old state of a domain to be shaken off (sometimes that's also the case when it was parked for a while)" (via Search Engine Journal).
4. So a page that is still "unknown" one to three weeks after a sitemap is inside the stated range. Wait, then check again (2.2). Don't change the page or the plan because of it.

### 2.4 Make the page worth finding

1. **Words people and agents use.** Get volumes from a keyword tool. Planner volumes are estimates. Once a page is indexed, Search Console's queries are the real figures.
2. **Original data earns links.** Pages with a fact nobody else has (a price survey, a scan count) get linked and cited more often. Most pages earn no links at all: 94% of blog posts have none (Backlinko, a study of 912M posts).
3. **Trust.** Google's raters treat trust as "the most important member of the E-E-A-T family". Raters grade results; they don't set rank. Keep a named author and real sources on every page anyway.
4. **On the page,** from Google's SEO Starter Guide:
   1. A title is "unique to the page, clear and concise, and accurately describes the contents of the page".
   2. The snippet usually comes from the page's own text. The meta description is used only sometimes, and should be "short, unique to one particular page".
   3. Link text tells users and Google what the linked page is. Link your own pages to each other with words that name the destination, not "click here".
   4. Informative images get alt text that explains what the image shows and how it relates to the page.
   5. Google ignores the keywords meta tag, and keyword stuffing is against its spam policies.
   6. Pages that repeat each other's content should redirect, or name one canonical URL.
   Practitioner guides say the same and add two habits worth keeping: map one search intent to one URL, and log every page change with its date (2.6.4).
5. **Structured data is for features, not rank.** "Google does not guarantee that your structured data will show up in search results." Dataset markup helps Dataset Search. Add it where a feature exists, never to rank.

### 2.5 Earn links, and count them yourself

1. A link counts only once the page carrying it is crawled, and crawlers visit well-linked pages first.
2. Find where competitors are linked, with a backlink tool.
3. Read how each linking page links (follow or not, priced entry or review).
4. Count your own links with your own re-fetch every week. Every engine's link report lags: Bing showed 0 links for a site while one was live.
5. Expect few. Ahrefs: "We sent 515 emails and got 36 backlinks from 32 websites", about 7%. 14 emails make about 1 link.
6. Paid links are link spam under Google's policies. Any paid placement carries `rel="sponsored"`.

### 2.6 Measure

1. People and agents on your pages: your analytics, leaving out your own visits and bots.
2. Queries and clicks: Search Console, once pages are indexed.
3. Links: your own link record (2.5.4).
4. Changes: when an indexed page's title, headings or main text change, log the page, the date and what changed. Without the date, a later rise or fall can't be tied to the change.
5. Once a page has impressions: queries where it sits at positions 5 to 20, or where it has many impressions and few clicks, are the first to work on. This is a practitioner's rule of thumb, not tested by us.

## 3. What we believe, and how sure

| # | Belief | Verdict | What to do |
|---|---|---|---|
| 1 | Get indexed before chasing links | supported | 2.1 to 2.3 come before 2.5 |
| 2 | A new link shows up in Ahrefs, Majestic or Moz | qualified: a link on an obscure page may never appear | read vendor reports as a floor |
| 3 | Links are how a new site is found | supported as one way of several | sitemap, IndexNow, internal links first |
| 4 | Doing it all right guarantees indexing | contradicted by Google's own words | wait the stated range (2.3) |
| 5 | About 1 link from 14 outreach emails | supported (about 7%) | size outreach to it |
| 6 | Directories and badges are worthless | untested: no Google or Bing page says either way | a choice, not a finding; test before ruling out |
| 7 | Most pages earn no links | supported | write fewer, better pages |
| 8 | Original data earns links | supported, size unverified | 2.4.2 |
| 9 | Longer pages earn more links | qualified: correlation only | length is not a goal |
| 10 | Structured data helps | supported for features (Dataset Search); untested for rank | 2.4.5 |
| 11 | llms.txt helps AI citation | unsupported: proposed, no engine shown using it | keep it if cheap, spend no builder time on it |
| 12 | Trust drives quality | supported as Google's stated view | named author, real sources |
| 13 | Clicks reorder results | secondary only (readings of a 2024 leak) | don't plan on it |
| 14 | Planner volumes are right | untested | confirm with Search Console |
| 15 | Keyword research is the core skill | taught everywhere, not tested | do it (2.4.1), don't stop at it |
| 16 | SEO takes months | qualified: discovery takes hours to weeks (Google); ranking takes longer and is untested | judge discovery at weeks, ranking at months |
| 17 | Link building is taught, so it works | not evidence | judge by your own link count |

## 4. Open questions, each with its test

1. **Do directory listings help?** (row 6) List on two directories, then compare those pages' crawl and visit counts with unlisted ones after 30 days. Many directory links are nofollow: count visits as well as links.
2. **Are Planner volumes right?** (row 14) Compare them with Search Console impressions 30 days after a page is indexed.
3. **Does a domain's history slow it in Bing?** Compare how many pages Google and Bing index after two weeks on a domain that was parked for years.
