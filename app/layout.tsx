import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "123KozijnenVergelijker | Vergelijk kunststof kozijnen",
  description:
    "Vergelijk kunststof kozijnen, deuren en schuifpuien en ontvang offertes van passende aanbieders in jouw regio.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="nl">
      <body>{children}</body>
    </html>
  );
}
