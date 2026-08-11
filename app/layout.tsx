import type { Metadata, Viewport } from "next";
import { JsonLd } from "../components/JsonLd";
import { globalSchema } from "../lib/schema";
import { SITE_NAME, SITE_URL } from "../lib/seo";
import "./globals.css";
import "./legacy.css";
import "./seo.css";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: "Kunststof kozijnen vergelijken | 123KozijnenVergelijker",
  description:
    "Vergelijk kunststof kozijnen, deuren en schuifpuien op prijs, kwaliteit, montage, garantie en voorwaarden. Gratis en vrijblijvend.",
  applicationName: SITE_NAME,
  manifest: "/manifest.webmanifest",
  alternates: { canonical: SITE_URL },
  icons: {
    icon: [{ url: "/icon.svg", type: "image/svg+xml" }],
    shortcut: "/icon.svg",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },
  openGraph: {
    type: "website",
    locale: "nl_NL",
    url: SITE_URL,
    siteName: SITE_NAME,
    title: "Kunststof kozijnen vergelijken | 123KozijnenVergelijker",
    description: "Vergelijk kunststof kozijnen, deuren en schuifpuien op prijs, kwaliteit, montage, garantie en voorwaarden.",
    images: [{ url: "/opengraph-image", width: 1200, height: 630, alt: "123KozijnenVergelijker – kunststof kozijnen vergelijken" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Kunststof kozijnen vergelijken | 123KozijnenVergelijker",
    description: "Vergelijk kunststof kozijnen, deuren en schuifpuien op prijs, kwaliteit, montage, garantie en voorwaarden.",
    images: ["/twitter-image"],
  },
};

export const viewport: Viewport = {
  themeColor: "#0c1b2f",
  colorScheme: "light",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="nl">
      <body>
        <JsonLd data={globalSchema()} />
        {children}
      </body>
    </html>
  );
}
