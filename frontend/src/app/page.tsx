"use client";

import { useState } from "react";

export default function Home() {

  const [resume, setResume] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [response, setResponse] = useState("");
  const handleAnalyze = async () => {
  if (!resume) {
    alert("Please upload a resume.");
    return;
  }

  const formData = new FormData();
  formData.append("file", resume);
  formData.append("job_description", jobDescription);

  try {
    const res = await fetch("http://127.0.0.1:8000/analyze-resume", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    if (data.response?.error) {
      setResponse("Gemini API Error:\n\n" + data.response.error);
    } else {
      setResponse(data.response || "No response received.");
    }

  } catch (error) {
    setResponse("Failed to connect to backend.");
  }
};

  return (
      <main className="min-h-screen flex flex-col items-center justify-center p-8 bg-gray-100 text-black">
      <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-2xl">
        <h1 className="text-3xl font-bold text-center mb-6 text-black">
          AI Resume Screener
        </h1>

        <div className="mb-5">
          <label className="block font-semibold mb-2 text-black">
            Upload Resume
          </label>
          <input
            type="file"
            className="border p-2 rounded w-full"
            onChange={(e) => {
              if (e.target.files) {
              setResume(e.target.files[0]);
              }
            }}
          />
        </div>

        <div className="mb-5">
          <label className="block font-semibold mb-2 text-black">
            Job Description
          </label>

          <textarea
            rows={8}
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            placeholder="Paste job description here..."
            className="border border-gray-400 p-2 rounded w-full text-black bg-white"
            />
        </div>

        <button
          onClick={handleAnalyze}
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            Analyze Resume
        </button>

        <div className="mt-8">
          <h2 className="font-bold text-xl mb-2">
            AI Response
          </h2>

          <div className="border border-gray-300 rounded p-4 bg-white text-black min-h-[120px] whitespace-pre-wrap">
            {response || "Response will appear here..."}
          </div>
        </div>
      </div>
    </main>
  );
}