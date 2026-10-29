# Runbook: set the visual hierarchy of a page

## 1. The lecture

1. **Course.** Department of Design, "Visual Communication", week 3: hierarchy. The question of the week: of everything on this screen, what does the viewer see first, second and last, and did you choose that order or did it happen?
2. **The idea and its names.** A visual hierarchy is the order in which a design guides the eye (Nielsen Norman Group, "Visual Hierarchy in UX": "A clear visual hierarchy guides the eye to the most important elements on the page. It can be created through variations in color and contrast, scale, and grouping."). The names the field uses:
   1. *Scale.* "Use no more than 3 sizes" and "Limit how many elements are big to a maximum of 2".
   2. *Contrast.* "Use no more than 3 contrast variations for complex designs. If everything is contrasted, then nothing stands out.".
   3. *Grouping, by proximity and by common region (enclosure).* "An element that has more space around it will be perceived as one group and thus will receive more attention.".
   4. *The squint test.* "we are taught to squint or apply a slight blur to the design to get an idea of the conveyed groupings and hierarchy".
   5. *Gestalt laws* (proximity, similarity, common region, closure) are the theory under grouping. Wertheimer and the Gestalt school are the real names.
   6. *A type scale of roles.* Heading, body, label and small print each get one size and weight, and the same role looks the same everywhere. "Use the fewest roles and families that make the hierarchy unmistakable. Combine size, weight, space, and tone deliberately instead of asking size alone to do all the work." (from the typesetting guidance in the impeccable design skill). It also asks whether "adjacent sizes or weights [are] too close to carry different jobs".
   7. *Two levels.* A page has a hierarchy between its sections (which section is loudest) and a hierarchy inside each section (what in it is seen first). Setting the first and skipping the second is how a page gets one good hero over a column of flat sections.
3. **What people look at first, from the studies**:
   1. *The first screen takes the most time.* NN/g, 120 participants, over 130,000 fixations on a 1920x1080 screen: "users spent about 57% of their page-viewing time above the fold. 74% of the viewing time was spent in the first two screenfuls, up to 2160px." In 2010 it was 80% above the fold. NN/g's own caveat: the analysis "disregards the maximum page length", so the two-screenful figure may be short pages or people giving up. The study is 2018 desktop; it does not say what a phone does.
   2. *Reserve the top for the main goal.* NN/g's advice from that study: "Reserve the top of the page for high-priority content: key business and user goals ... Keep major CTAs above the fold." and "Beware of false floors". This is NN/g's recommendation, not a measured conversion result.
   3. *Reading goes in an F-ish shape.* NN/g recorded 232 users on thousands of pages; they read across the top, then a shorter bar lower down, then down the left side. "The F viewing pattern is a rough, general shape rather than a uniform, pixel-perfect behavior." The study covered text-heavy pages: an about-us article, a product page and a search results page. Do not take it as a layout for a hero.
   4. *Images: people look at images that carry information and ignore decoration.* "users ignore stock photos of generic people" and "pay attention to information-carrying images that show content that's relevant to the task at hand". Real employee portraits are the exception NN/g names.
   5. *A face does not pull more people to a low-attention area.* Djamasbi, Siegel and Tullis (2012), two eye-tracking studies: "faces did not increase the number of people who viewed the areas where the faces were located", though faces "affected fixation patterns on these areas", and a face above the fold lowered task performance. That is against the habit of putting a face to win attention; a face earns trust once seen, it does not earn the look.
   6. *Looks are judged in a blink.* Lindgaard et al. (2006), Behaviour & IT 25:115-126: visual appeal ratings after 50 ms matched ratings after longer viewing; the authors argue a halo carries over to judgments of usability and credibility. The study measured appeal ratings, not trust or purchase.
   7. *Sparse pages may scan differently from text pages.* Design courses teach a Z-shaped path for sparse layouts such as a hero (top left, top right, across, bottom right). It is a teaching shape, not a study we have read.
4. **The classic mistakes.**
   1. Everything is emphasised, so nothing is (NN/g, 2.2 above).
   2. Using colour alone to rank things (NN/g: "Do not rely only on color").
   3. A decorative hero or a stock "team" photo where an informative picture could go (2.4 above).
   4. Judging the page on your own large screen, where it looks complete (you read everything; the visitor holds one phone screen).
   5. Designing the template and not the content that fills it (NN/g, same page: "it's not enough to design the template — you must also consider the content that will fill it").
   6. Setting the hierarchy of the page and not inside each section (1.2.7).
   7. Sizes and weights that are close but not equal, so two roles look like one mistake (1.2.6).
5. **Readings.** NN/g, *Visual Hierarchy in UX*; NN/g, *Scrolling and Attention*; NN/g, *F-Shaped Pattern of Reading on the Web*; NN/g, *Photos as Web Content*; Djamasbi, Siegel and Tullis (2012), *Faces and Viewing Behavior*.

## 2. The steps

Synthesis. Each step names what justifies it.

1. **Say the order in words first, at both levels.** For one persona on the phone screen, write "first they see X, then Y, then Z" for the sections down the page. Then list the sections (the inventory of its sections) and write the same sentence for each section, one at a time. If you cannot rank them, the design will not. Justified by 1.1 and 1.2.7.
2. **Pick at most one large thing and at most three sizes, as a role scale.** One hero element is the biggest on the page; sizes are small, medium, large, each tied to a role that looks the same in every section. Justified by 1.2.1 and 1.2.6.
3. **Spend contrast once.** Choose the one element that is the loudest by value and saturation (the action, or the proof of the work). Everything else shares a quiet treatment. Justified by 1.2.2 and 1.4.1.
4. **Group by space and enclosure before you add rules and labels.** Related things sit closer to each other than to the next group; use a panel only where a group needs to read as one thing. Justified by 1.2.3.
5. **Put the picture of the work where the eye lands, and make it carry information.** A real before and after, a real person who works there, a real price. Not a mood. Justified by 1.3.4 and 1.3.5 (a face placed to attract does not attract; it is read once seen).
6. **Put the main goal and the main action in the first screen, and show a cut edge.** Cut a row at the fold so the page signals more below. Justified by 1.3.1 and 1.3.2.
7. **Squint test, at two widths, for the page and for each section.** Blur a screenshot at 390 and at 1280; write down what you can still see, in order, and compare it to step 1. Then do the same for each section's own screenshot. If they differ, the page, not your words, is the truth. Justified by 1.2.4.
8. **Do not call it done on your own eyes.** A model prompted as your one persona and shown each part of a screenshot is a cheap per-section check; it says where a model would look. A person outside the team is the only evidence. Justified by 1.3.6 (the blink measures appeal, not trust).

## 3. What is untested

1. All the studies are desktop, 2018 or earlier on the F-pattern and faces. No phone eye-tracking study was found.
2. The claim that putting trust content in the first screen raises replies is a bet. It has not been tested with real visitors.
3. The step 7 squint test is NN/g's own teaching, not a measured gain.
4. Lindgaard (2006) and Gestalt are unread. The Z-pattern (1.3.7) is unread.
