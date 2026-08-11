import type { MetadataRoute } from "next";
import fs from "node:fs";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = "https://www.123kozijnenvergelijker.nl";
  const pages = fs
    .readdirSync(process.cwd())
    .filter((name) => name.endsWith(".html"))
    .filter((name) => !["index.html", "blog-detail.html", "lander.html", "lp-kozijnen.html"].includes(name));

  return [
    { url: base, changeFrequency: "weekly", priority: 1 },
    ...pages.map((page) => ({
      url: `${base}/${page}`,
      changeFrequency: page.startsWith("kozijnen-") ? ("monthly" as const) : ("monthly" as const),
      priority: ["kunststof-kozijnen.html", "kunststof-deuren.html", "kunststof-schuifpuien.html", "offerte-aanvragen.html"].includes(page) ? 0.9 : 0.7,
    })),
  ];
}
