import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "123KozijnenVergelijker",
    short_name: "123Kozijnen",
    description: "Vergelijk kunststof kozijnen, deuren en schuifpuien op prijs, kwaliteit en voorwaarden.",
    start_url: "/",
    display: "standalone",
    background_color: "#ffffff",
    theme_color: "#0c1b2f",
    lang: "nl-NL",
    icons: [
      {
        src: "/icon.svg",
        sizes: "any",
        type: "image/svg+xml",
        purpose: "any",
      },
    ],
  };
}
