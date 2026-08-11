import { ImageResponse } from "next/og";

export const alt = "123KozijnenVergelijker – kunststof kozijnen vergelijken";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          background: "linear-gradient(135deg,#0c1b2f 0%,#132f45 58%,#1f8a70 100%)",
          color: "white",
          padding: "72px 80px",
          position: "relative",
          fontFamily: "Arial, sans-serif",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column", justifyContent: "space-between", width: "100%" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
            <div style={{ width: 78, height: 78, borderRadius: 20, background: "#1f8a70", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 31, fontWeight: 800 }}>123</div>
            <div style={{ display: "flex", fontSize: 30, fontWeight: 700 }}>
              Kozijnen<span style={{ color: "#9ad6c5" }}>Vergelijker</span>
            </div>
          </div>
          <div style={{ display: "flex", flexDirection: "column", maxWidth: 890 }}>
            <div style={{ color: "#9ad6c5", fontSize: 22, textTransform: "uppercase", letterSpacing: 2, marginBottom: 20 }}>Slim vergelijken</div>
            <div style={{ fontSize: 66, lineHeight: 1.05, fontWeight: 800, letterSpacing: -3 }}>Vergelijk kunststof kozijnen op wat écht telt.</div>
            <div style={{ color: "#d7e2e9", fontSize: 25, marginTop: 24 }}>Prijs · glas · profiel · montage · garantie · voorwaarden</div>
          </div>
        </div>
      </div>
    ),
    size,
  );
}
