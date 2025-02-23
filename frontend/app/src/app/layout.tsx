// app/layout.tsx
import './globals.css';

export const metadata = {
  title: 'My Recommendation App',
  description: 'A Next.js app to display recommendations',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
