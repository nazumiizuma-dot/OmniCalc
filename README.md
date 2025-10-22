# OmniCalc-Pro (Early Prototype)
This is a ready-to-run prototype of OmniCalc Pro (FastAPI backend + Next.js frontend).
## Quickstart
1. Copy env:
   cp backend/.env.example backend/.env
   (edit backend/.env to add OPENAI_API_KEY if you want online AI)
2. Start:
   docker-compose up --build
3. Open frontend: http://localhost:3000
   API docs: http://localhost:8000/docs
## Notes
- The offline AI is a simple fallback. For production, integrate a proper local LLM or isolate execution for user-submitted code.
- No secrets are included. Put secrets in backend/.env or your secret manager.
## 💻 OmniCalc — Smart Web Calculator Powered by AI
## 🧠 Deskripsi Karya
**OmniCalc** adalah proyek berbasis **Python dan Website** yang dirancang untuk menjawab kebutuhan sehari-hari di bidang perhitungan — baik itu di sekolah, pekerjaan, maupun kegiatan produktif lainnya.  
Tujuannya simpel: biar siapa pun bisa ngitung apa aja tanpa ribet, dengan tampilan modern dan responsif.
Proyek ini terdiri dari dua bagian utama:
- **Backend (Python FastAPI)** — buat ngatur semua logika perhitungan seperti matematika, fisika, keuangan, sampai konversi satuan.
- **Frontend (Next.js + TailwindCSS)** — buat tampilan web interaktif yang bisa diakses dari laptop maupun smartphone.
Selain itu, proyek ini juga **mengoptimalkan keberadaan AI**, di mana AI-nya bisa bantu pengguna memilih jenis kalkulator yang sesuai sama kebutuhan mereka, misalnya menghitung bunga majemuk, integral, statistik, atau bahkan analisis sederhana berbasis data input pengguna.
## 💡 Latar Belakang & Ide
Sebenernya ide awal muncul dari hal yang sederhana — banyak orang (terutama pelajar atau mahasiswa) yang masih repot buka banyak tab cuma buat ngitung hal-hal berbeda: kadang pakai kalkulator online, kadang Excel, kadang nyari rumus di Google.
Jadi daripada nyebar ke mana-mana, aku bikin satu platform yang bisa jadi **“pusat hitung universal”** — satu tempat buat semua jenis perhitungan.  
Dari perhitungan dasar kayak aritmatika dan trigonometri, sampai yang agak advance kayak kalkulus, statistik, dan keuangan modern.
Meskipun saya pribadi lebih tertarik ke dunia **finance makro-mikro dan ekonomi global**, proyek ini tetap saya kerjakan sebagai bentuk eksperimen dan pembuktian konsep: bahwa AI bisa bantu menyederhanakan cara kita berinteraksi dengan perhitungan kompleks tanpa harus paham coding atau matematika tingkat tinggi. Dan saya tidak berniat untuk
## 🎯 Manfaat
- Membantu pelajar atau mahasiswa ngerjain soal hitungan tanpa pindah-pindah aplikasi.  
- Bikin perhitungan cepat buat profesional di bidang sains, teknik, atau bisnis.  
- Memperkenalkan integrasi AI di aplikasi sederhana berbasis web.  
- Bisa dikembangkan lagi jadi platform edukasi interaktif berbasis AI di masa depan.
- Segini aja karena aku malas dan benci coding karena gak berguna di hidupku, see you, if we meet again 👋
