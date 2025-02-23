// app/api/recommendations/route.ts
import type { NextRequest } from 'next/server';

export async function GET(request: NextRequest) {
  // Extract user_id from the incoming request query parameters if available,
  // or fallback to a default value for testing purposes.
  const { searchParams } = new URL(request.url);
  const userId = searchParams.get('user_id') || '123'; // Use a default user id if none provided

  try {
    // Include the user_id query parameter when calling your backend
    const response = await fetch(`http://localhost:5000/api/recommendations?user_id=${userId}`, {
      headers: {
        'Accept': 'application/json',
      },
    });

    if (!response.ok) {
      console.error(`Backend responded with status ${response.status}: ${response.statusText}`);
      throw new Error('Failed to fetch recommendations');
    }

    const recommendations = await response.json();
    return new Response(JSON.stringify(recommendations), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error: any) {
    console.error(error);
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
