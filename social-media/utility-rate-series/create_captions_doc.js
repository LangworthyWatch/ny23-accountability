const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  HeadingLevel, BorderStyle, PageBreak, LevelFormat,
  Header, Footer, PageNumber
} = require("docx");

// --- Caption data in posting-schedule order ---

const phases = [
  {
    title: "Phase 1: Set the Frame (Days 1\u20132)",
    posts: [
      {
        heading: "Day 1 \u2014 Post 0: What Is Regulatory Capture?",
        image: "post00_regulatory_capture.png",
        caption: [
          "What is regulatory capture?",
          "It\u2019s when the agency meant to regulate an industry is instead controlled by it.",
          "Here\u2019s how it works with your electric bill in New York \u2014 every step documented with public data:",
          "1. LOBBY \u2014 Energy companies spent $75.7M lobbying Albany. 87.7% on rate-case policy.\n2. APPOINT \u2014 The Governor appoints all 7 PSC commissioners who set your rates.\n3. REVOLVE \u2014 The PSC Chair previously worked at KeySpan Energy (now National Grid).\n4. APPROVE \u2014 The PSC approves rate increases with a guaranteed 9% profit for shareholders.\n5. PROFIT \u2014 Shareholders received $36.8B in dividends. CEO pay grew 64%. Your rates: 42%.\n6. BLAME \u2014 Utilities blame \u201Cclean energy\u201D \u2014 which is 4.7% of the increase.",
          "Over the next week, we\u2019ll show you the data behind every step.",
          "Sources: COELIG/JCOPE lobbying, PSC commissioner bios, FERC Form 1, EIA\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#RegulatoryCapture #UtilityRates #NewYork #PSC #FollowTheMoney #DataJournalism"
        ]
      },
      {
        heading: "Day 2 (AM) \u2014 Post 1: 4.7% (The Hook)",
        image: "post01_hook_4.7pct.png",
        caption: [
          "New York\u2019s electricity rates are 49.7% above the national average. Politicians keep blaming clean energy mandates.",
          "We analyzed 8 utility rate case filings totaling $4 BILLION in requested increases.",
          "\u2192 Clean energy programs: 4.7% ($187M)\n\u2192 Infrastructure & capital: 33.7% ($1,355M)\n\u2192 Shareholder profit guarantees: 10.1% ($408M)",
          "The clean energy surcharge adds about $3.36/month to your bill.",
          "Full data investigation with downloadable source files at langworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#NYS #UtilityRates #NYSEG #NY23 #FactCheck #CleanEnergy #DataJournalism"
        ]
      },
      {
        heading: "Day 2 (PM) \u2014 Post 2: Where Your Rate Increase Actually Goes",
        image: "post02_breakdown.png",
        caption: [
          "Your utility filed for a rate increase. Here\u2019s what they said they need the money for.",
          "Notice anything? The thing politicians talk about most \u2014 clean energy \u2014 is the smallest bar.",
          "Source: PSC rate case filings (dps.ny.gov), 8 cases, 2023\u20132025\nFull breakdown + downloadable data: langworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#UtilityBills #NewYork #RateIncrease #PSC #NYSEG #DataDriven"
        ]
      }
    ]
  },
  {
    title: "Phase 2: The Deep Dive (Days 3\u20136)",
    posts: [
      {
        heading: "Day 3 \u2014 Post 4: $3.36/month (The Squeeze)",
        image: "post04_monthly.png",
        caption: [
          "The System Benefits Charge \u2014 the \u201Cclean energy surcharge\u201D \u2014 adds about $3.36/month to your bill.",
          "NYSEG is requesting a rate increase that would add $21.53/month.",
          "If you eliminated the clean energy surcharge entirely, you\u2019d save $3.36/month.\nIf NYSEG\u2019s infrastructure request gets approved, you\u2019d pay $21.53/month more.",
          "Which problem should Congress focus on?",
          "Source: PSC rate case 25-E-0375\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#NYSEG #ElectricBill #SouthernTier #NY23"
        ]
      },
      {
        heading: "Day 4 \u2014 Post 3: CEO Pay vs. Your Bill (The Gap)",
        image: "post03_ceo_gap.png",
        caption: [
          "Between 2015 and 2024:",
          "\u2192 CEO compensation at NY\u2019s top 3 utilities grew 64%\n\u2192 Your electricity rates grew 42%\n\u2192 National Grid\u2019s CEO alone: +78.6%",
          "Shareholders received $36.8 BILLION in dividends \u2014 that\u2019s 5.3x more than the total clean energy surcharge.",
          "But sure. It\u2019s the solar panels.",
          "Source: SEC DEF 14A proxy statements, FERC Form 1\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#ExecutivePay #UtilityProfits #NationalGrid #NewYork"
        ]
      },
      {
        heading: "Day 5 \u2014 Post 5: Upstate Pays More (The Burden)",
        image: "post05_burden.png",
        caption: [
          "Electricity costs take a bigger bite in lower-income communities.",
          "\u2192 Lowest income quartile: 2.99% of annual income on electricity\n\u2192 Highest income quartile: 1.85%",
          "NYSEG \u2014 which serves Steuben, Chemung, Tioga, Allegany, and other Southern Tier counties \u2014 is requesting the steepest increase at 18.4%.",
          "The counties that can afford it least get hit the hardest.",
          "Source: EIA electricity prices, Census ACS 2022\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#SouthernTier #NY23 #NYSEG #RuralNY"
        ]
      },
      {
        heading: "Day 6 \u2014 Post 7: $75.7 Million (The Machine)",
        image: "post07_lobbying.png",
        caption: [
          "New York\u2019s energy companies spent $75.7 million lobbying in Albany over the past decade.",
          "\u2192 87.7% of that ($62.9M) was specifically about rate cases and energy policy\n\u2192 Annual lobbying spend nearly tripled from 2011 to 2024\n\u2192 Top spenders: Business Council $8.9M, Entergy $5.6M, National Grid $5.5M",
          "All 7 PSC commissioners who approve rate increases are appointed by the Governor.",
          "Source: COELIG/JCOPE lobbying disclosures\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#Lobbying #Albany #RateCase #PSC #FollowTheMoney"
        ]
      }
    ]
  },
  {
    title: "Phase 3: Accountability (Days 7\u20139)",
    posts: [
      {
        heading: "Day 7 \u2014 Post 6: Complaints +84%",
        image: "post06_complaints.png",
        caption: [
          "People are telling regulators they can\u2019t afford their bills. The regulators are hearing them \u2014 but the utilities keep filing for more.",
          "\u2192 Statewide complaints: 24,146 \u2192 44,538 (2019\u20132024)\n\u2192 Billing complaints grew 120% \u2014 3.2x faster than service complaints\n\u2192 NYSEG and RG&E: ~95% complaint growth. Same parent company now requesting 18% rate increase.",
          "Source: PSC consumer complaint data, 2019\u20132024\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "#PSC #ConsumerProtection #UtilityBills"
        ]
      },
      {
        heading: "Day 8 \u2014 Post 8: 18.4% (The Silence)",
        image: "post08_silence.png",
        caption: [
          "NYSEG \u2014 the utility serving most of NY-23 \u2014 is requesting an 18.4% rate increase.",
          "That\u2019s the steepest pending increase of any major utility in the state.",
          "Rep. Langworthy has repeatedly blamed clean energy mandates for high bills. He has not publicly addressed the NYSEG rate case currently before the PSC.",
          "Of NYSEG\u2019s rate increase request, clean energy programs account for 4.7%. Infrastructure and capital investment: 33.7%.",
          "langworthywatch.org/fact-checks/2026-02-25-nyseg-rate-hike-silence/",
          "#NY23 #NYSEG #RateHike #Accountability"
        ]
      },
      {
        heading: "Day 9 (AM) \u2014 Post 9: Avangrid \u2192 Langworthy (The Connection)",
        image: "post09_connection.png",
        caption: [
          "Avangrid \u2014 the parent company of NYSEG \u2014 donated to Langworthy\u2019s congressional campaign.",
          "Avangrid is currently requesting an 18.4% rate increase that would hit NY-23\u2019s lowest-income counties the hardest.",
          "The donation is small ($1,500). The silence is louder.",
          "Source: FEC individual contributions, C00817932\nlangworthywatch.org/fact-checks/2026-02-25-nyseg-rate-hike-silence/",
          "#FollowTheMoney #NY23 #NYSEG #CampaignFinance"
        ]
      },
      {
        heading: "Day 9 (PM) \u2014 Post 10: Read the Full Investigation (The CTA)",
        image: "post10_cta.png",
        caption: [
          "We published the full data investigation with:",
          "\u2192 6 interactive charts\n\u2192 4 downloadable CSV datasets\n\u2192 Every source linked\n\u2192 No paywalls, no ads, no party affiliation",
          "Who\u2019s really driving your electric bill?\nlangworthywatch.org/fact-checks/2026-03-14-nys-utility-rates-data-investigation/",
          "Share if you think your neighbors should see this data.",
          "#LangworthyWatch #DataJournalism #Transparency #NY23"
        ]
      }
    ]
  }
];

// --- Build document ---

function makeSeparator() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: "CCCCCC", space: 1 }
    },
    children: []
  });
}

// Convert caption text (which may contain \n) into an array of Paragraphs
function captionToParagraphs(lines) {
  const paragraphs = [];
  for (const line of lines) {
    const sublines = line.split("\n");
    for (const sub of sublines) {
      const isHashtags = sub.startsWith("#");
      paragraphs.push(
        new Paragraph({
          spacing: { after: isHashtags ? 0 : 120 },
          children: [
            new TextRun({
              text: sub,
              font: "Calibri",
              size: 22, // 11pt
              color: isHashtags ? "2B6CB0" : "1A202C",
              italics: isHashtags
            })
          ]
        })
      );
    }
  }
  return paragraphs;
}

const children = [];

// Title
children.push(
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 80 },
    children: [
      new TextRun({
        text: "Utility Rate Series",
        font: "Calibri",
        size: 48, // 24pt
        bold: true,
        color: "1E3A5F"
      })
    ]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 60 },
    children: [
      new TextRun({
        text: "Social Media Captions",
        font: "Calibri",
        size: 36, // 18pt
        color: "1E3A5F"
      })
    ]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 300 },
    children: [
      new TextRun({
        text: "Instagram + Facebook  |  11 Posts over 9 Days",
        font: "Calibri",
        size: 24, // 12pt
        color: "718096"
      })
    ]
  }),
  makeSeparator()
);

for (let pi = 0; pi < phases.length; pi++) {
  const phase = phases[pi];

  // Phase heading
  children.push(
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 360, after: 240 },
      children: [
        new TextRun({
          text: phase.title,
          font: "Calibri",
          size: 32, // 16pt
          bold: true,
          color: "1E3A5F"
        })
      ]
    })
  );

  for (let i = 0; i < phase.posts.length; i++) {
    const post = phase.posts[i];

    // Day heading
    children.push(
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [
          new TextRun({
            text: post.heading,
            font: "Calibri",
            size: 28, // 14pt
            bold: true,
            color: "2B6CB0"
          })
        ]
      })
    );

    // Image filename
    children.push(
      new Paragraph({
        spacing: { after: 160 },
        children: [
          new TextRun({
            text: "Image: ",
            font: "Calibri",
            size: 20, // 10pt
            color: "718096",
            italics: true
          }),
          new TextRun({
            text: post.image,
            font: "Calibri",
            size: 20,
            color: "718096",
            italics: true
          })
        ]
      })
    );

    // Caption paragraphs
    const captionParas = captionToParagraphs(post.caption);
    children.push(...captionParas);

    // Separator between posts
    children.push(makeSeparator());
    // Page break after each post except the very last
    if (!(pi === phases.length - 1 && i === phase.posts.length - 1)) {
      children.push(new Paragraph({ children: [new PageBreak()] }));
    }
  }
}

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Calibri", size: 22 }
      }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Calibri", color: "1E3A5F" },
        paragraph: { spacing: { before: 360, after: 240 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Calibri", color: "2B6CB0" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 }
      }
    ]
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              alignment: AlignmentType.RIGHT,
              children: [
                new TextRun({
                  text: "LangworthyWatch.org \u2014 Utility Rate Series",
                  font: "Calibri",
                  size: 18,
                  color: "718096",
                  italics: true
                })
              ]
            })
          ]
        })
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({ text: "Page ", font: "Calibri", size: 18, color: "718096" }),
                new TextRun({ children: [PageNumber.CURRENT], font: "Calibri", size: 18, color: "718096" })
              ]
            })
          ]
        })
      },
      children
    }
  ]
});

const outputPath = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/Utility_Rate_Series_Captions.docx";

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log("Created: " + outputPath);
});
