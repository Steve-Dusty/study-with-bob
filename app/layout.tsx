import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Study With Bob - AI-Powered Learning Platform",
  description: "An intelligent learning platform for students and teachers",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

