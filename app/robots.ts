import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
    sitemap: "https://www.123kozijnenvergelijker.nl/sitemap.xml",
    host: "https://www.123kozijnenvergelijker.nl",
  };
}
