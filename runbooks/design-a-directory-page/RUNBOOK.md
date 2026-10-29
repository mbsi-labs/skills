# Runbook: design a directory page that a stranger scans to pick one entry

A directory is an index of many entries of one kind (skills, plugins, tools, crates) where the reader's job is to pick the one that fits the job in front of them, then leave the index. The page is judged by whether the right entry is found and trusted, not by how long the reader stays.

## 1. The lecture

1. **Course.** School of Information, "Information Seeking and Interface Design", week 6: the index page. The question of the week: a person with a job, not an entry, in mind has seconds. What on the index lets them rule entries in and out without opening them?
2. **Information scent.** "When deciding which links to click on the web, users choose those with the highest information scent — which is a mix of cues that they get from the link label, the context in which the link is shown, and their prior experiences." (Nielsen Norman Group, "Information Scent"). Its first implication: "Summary text for an article or page should convey the gist of that information source and add detail to the link label.". Pirolli and Card's information foraging (CHI 1995) is the source theory.
3. **Do not hide the way in on desktop.** Hidden menus were used in 27% of cases on desktop, against 48% for visible navigation, in an NN/g study of 179 people (Nielsen Norman Group, on hamburger menus). A directory's filters are the way in, so they stay visible on desktop.
4. **Do not cite Hick's law for a number of items.** The evidence is old and thin and the abstract gives no figure (Hick, 1952).
5. **Where readers arrive.** Many land mid-site from a search or an agent's link. The page should say where it is and what it is a list of (Nielsen Norman Group, "You Are Here": "search engines can drop your website visitors anywhere").
6. **Seen by a person, not read.** Five real directories at 1440x900 on 2026-10-28 (skills.sh, cursor.directory, smithery.ai, crates.io, Raycast store). Observed there: all five are dark; search sits above the list; the two largest lists use hairline rows, not cards; popularity numbers lead; none says what an entry fixes before the click; one opens with a modal. This is one person's look on one day, not a study.
7. **Unchecked:** that rows beat cards as a list grows; that filter counts help the reader decide; that showing an entry's own text on the index raises the right pick (one model's invention until a real person tests it). See step 11.

## 2. Classic mistakes students make

1. Ranking by popularity numbers the owner does not have. For a young directory the numbers are zero, or invented, and the reader can tell.
2. A uniform grid of name-and-blurb cards: every entry looks the same, so the reader has only the names to judge by (the information scent is only the label).
3. A blurb that says what the entry is called, not what it is for ("Java rules and best practices for Cursor").
4. A filter rail built for dozens of entries that sits empty beside three.
5. An "add this" control on the index, before the reader can see what "this" is.
6. A modal, banner or slide-in on arrival (see smithery in the lecture, item 6).
7. Dark theme copied from the neighbours when the site's own shared parts are light. A directory inside a site wears the site's shell.

## 3. The steps

1. **Find the collection's shape first.** If the entries link to each other (one calls another, chains, bundles, shared sources), the directory is a graph, not a list. Lead with an Obsidian-style graph of the real links, entries as nodes and links as edges, drawn from data, never by hand: it is the viewer moment (a viewer screen shows a mass of real data), and it is the altitude a flat list misses. Each entry's page carries what it links to and what links to it.
2. **Frame it.** The one persona, what they ask, and what the entry is judged by. Write the brief first; a design turn with the persona is a hypothesis to test, not a requirement.
3. **Name the entry's unit of scent.** Decide which one sentence and which one block of the entry's own text the index shows. Use only what is true today. If a field would be empty (version, changelog, installs, ranking), do not draw a slot for it.
4. **Use the collection's own organization as its categories,** when it has one (our skills are already organized by kit, plus a global set). The directory's front page is an overview: what the collection is, how to install it, how it is made and why it is published; it points at the categories, and each category page lists its entries. Never flatten a structured collection into one list.
5. **Give every entry and every group a picture.** People navigate an index by images before words: an icon per group and a picture per entry, inside the card, with a soft gradient where the image meets the text (images are for speed and ease). The greybox draws each image as a labelled grey box at its real size. Then choose the row or card around the picture.
6. **Give the reader somewhere to rest.** Generous whitespace around the index and between entries; the desktop canvas spent on room, not packed with more rows. Ask of every screen "where can they rest?" (pages built by agents forget the reader's rest).
7. **Search and filters.** Search at the top and visible. Filters appear when the count earns them: draw the page at the launch count and at ten times that, and check both look right (the greybox shows both).
8. **First screen.** The reader sees what the list is of, how many, the grouping, and at least one full entry (name, sentence, block) with no scroll at 1280x800. Nothing covers it.
9. **Keep the site's shared parts.** Header, nav, footer and colours are the site's own Build each one once and use it in every view..
10. **Greybox on the desktop canvas,** grey only, then set the visual hierarchy and judge whether the page looks dated, then get the owner's explicit approval before any colour.
11. **Test the two tests.** gutcheck as the design persona and as the affordance persona. Whatever they say about rows against cards, or about showing the text, goes in section 1.7 as an observation with its date; it stays unchecked until a real reader is watched.

## 4. Open questions

1. Whether rows beat cards, whether counts help, and whether showing an entry's own text helps: unchecked (1.7).

