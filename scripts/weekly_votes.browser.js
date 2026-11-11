// Weekly votes pull for the "This week in NY-23" roundup.
// Run in the built-in browser on a clerk.house.gov page (the Clerk serves the XML to a real browser
// session; curl gets a bot challenge, and we do not try to get around it). Paste into javascript_tool.
// Set FROM to the first roll call of the week; it walks forward until a roll number does not exist.
const YEAR = 2026, FROM = 315, ME = 'L000600';
const out = [];
for (let n = FROM; n < FROM + 120; n++) {
  const r = await fetch(`https://clerk.house.gov/evs/${YEAR}/roll${String(n).padStart(3, '0')}.xml`);
  if (!r.ok) break;
  const t = await r.text();
  if (!t.includes('<rollcall-vote')) break;
  const g = k => (t.match(new RegExp('<' + k + '>([^<]*)')) || [, ''])[1];
  out.push({
    roll: n, date: g('action-date'), measure: g('legis-num'), question: g('vote-question'),
    desc: g('vote-desc').slice(0, 120), result: g('vote-result'),
    totals: ((t.match(/<totals-by-vote>[\s\S]*?<\/totals-by-vote>/) || [''])[0]).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').replace('Totals', '').trim(),
    his_vote: (t.match(new RegExp('name-id="' + ME + '"[\\s\\S]{0,300}?<vote>([^<]*)')) || [, 'NOT FOUND'])[1]
  });
}
({ count: out.length, cast: out.filter(o => o.his_vote !== 'Not Voting').length, rolls: out })
