import React from "react";

export default function HealthBar({ score }) {
  return (
    <div style={{ background: "#dbeafe", height: "12px" }}>
      <div
        style={{
          width: `${score}%`,
          background: "#1e3a8a",
          height: "100%",
        }}
      />
    </div>
  );
}