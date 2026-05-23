"""
AdiZenWorks Cybersecurity Toolkit V1 — Desktop GUI
Brand: Burgundy · Crimson · Deep Space Black · Pearl White
Author: AdiZenWorks Inc.

Tools:
  1. Port Scanner       (adizenscanner)
  2. System Auditor     (adizenauditor)
  3. Web Spider         (adizenspider)
  4. Hash Generator     (adizenhasher)
  5. Password Cracker   (adizencracker)
  6. File Inspector     (adizeninspector)
  7. Data Filter        (adizenfilter)
  8. Hello / Env Check  (adizenhello)
"""

import sys
import os
import threading
import json
import datetime
from pathlib import Path

# ── PATH SETUP ────────────────────────────────────────────────
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

try:
    from adizen_cyber_toolkit import (
        adizenscanner,
        adizenauditor,
        adizenspider,
        adizenhasher,
        adizencracker,
        adizeninspector,
        adizenfilter,
        adizenhello,
    )
    MODULES_OK = True
    IMPORT_ERROR = ""
except ImportError as e:
    MODULES_OK = False
    IMPORT_ERROR = str(e)


# ── BRAND PALETTE ─────────────────────────────────────────────
C = {
    "bg":       "#080808",
    "bg2":      "#0f0f0f",
    "bg3":      "#161616",
    "bg4":      "#1e0808",
    "burgundy": "#6d0a1b",
    "crimson":  "#cc0000",
    "crimson2": "#ff2222",
    "crimson3": "#8b0000",
    "pearl":    "#e8e4dc",
    "muted":    "#887878",
    "border":   "#2a0a0a",
    "border2":  "#3a0000",
    "success":  "#00cc55",
    "warn":     "#cc8800",
    "info":     "#4488ff",
}


class AdiZenV1Desktop:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("AdiZenWorks Cybersecurity Toolkit V1.0 — Desktop")
        self.root.geometry("1300x840")
        self.root.minsize(1050, 700)
        self.root.configure(bg=C["bg"])

        # Window icon + header logo
        self._logo_img = None
        self._icon_img = None

        # Try to load logo for header (42px pre-scaled)
        logo_candidates = [
            project_root / "assets" / "logo_header.png",
            project_root / "assets" / "logo_small.png",
            project_root / "assets" / "adizenworks-logo.png",
            project_root / "adizenworks-logo.png",
        ]
        for logo_path in logo_candidates:
            if logo_path.exists():
                try:
                    img = tk.PhotoImage(file=str(logo_path))
                    # If image is larger than 48px, subsample it
                    if img.width() > 48:
                        factor = max(1, img.width() // 42)
                        img = img.subsample(factor, factor)
                    self._logo_img = img
                    break
                except Exception:
                    pass

        # Window icon (use full-res logo)
        for icon_path in [
            project_root / "assets" / "logo.png",
            project_root / "assets" / "adizenworks-logo.png",
            project_root / "adizenworks-logo.png",
        ]:
            if icon_path.exists():
                try:
                    ico = tk.PhotoImage(file=str(icon_path))
                    self.root.iconphoto(True, ico)
                    break
                except Exception:
                    pass

        self._build_ui()
        if not MODULES_OK:
            self.log(f"[ERROR] Import failed: {IMPORT_ERROR}", "err")

    # ═══════════════════════════════════════════════════════════
    # LAYOUT
    # ═══════════════════════════════════════════════════════════
    def _build_ui(self):
        # ── HEADER ──
        header = tk.Frame(self.root, bg=C["bg2"], height=58)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)

        left_h = tk.Frame(header, bg=C["bg2"])
        left_h.pack(side=tk.LEFT, padx=20, pady=8)
        # Logo in header
        if self._logo_img:
            logo_lbl = tk.Label(left_h, image=self._logo_img, bg=C["bg2"], bd=0)
            logo_lbl.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(left_h, text="AdiZenWorks", bg=C["bg2"], fg=C["pearl"],
                 font=("Segoe UI", 15, "bold")).pack(side=tk.LEFT)
        tk.Label(left_h, text="  Cybersecurity Toolkit  V1.0", bg=C["bg2"], fg=C["muted"],
                 font=("Segoe UI", 10)).pack(side=tk.LEFT)

        right_h = tk.Frame(header, bg=C["bg2"])
        right_h.pack(side=tk.RIGHT, padx=20)
        self.status_lbl = tk.Label(right_h, text="● READY", bg=C["bg2"], fg=C["success"],
                                   font=("Consolas", 9))
        self.status_lbl.pack(side=tk.RIGHT)

        tk.Frame(self.root, bg=C["crimson"], height=2).pack(fill=tk.X)

        # ── BODY ──
        body = tk.Frame(self.root, bg=C["bg"])
        body.pack(fill=tk.BOTH, expand=True)

        # ── SIDEBAR ──
        sidebar = tk.Frame(body, bg=C["bg2"], width=195)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        tk.Frame(sidebar, bg=C["border"], height=1).pack(fill=tk.X)

        self._nav_items = [
            ("🔌", "Port Scanner",      "scanner"),
            ("🔍", "System Auditor",    "auditor"),
            ("🕷", "Web Spider",        "spider"),
            ("🔐", "Hash Generator",    "hasher"),
            ("💀", "Password Tester",   "cracker"),
            ("📂", "File Inspector",    "inspector"),
            ("🧹", "Data Filter",       "filter"),
            ("👋", "Env Check",         "hello"),
        ]

        self._nav_btns = {}
        self._active = tk.StringVar(value="scanner")

        for icon, label, key in self._nav_items:
            btn = tk.Button(
                sidebar,
                text=f"  {icon}  {label}",
                bg=C["bg2"], fg=C["muted"],
                font=("Segoe UI", 9),
                anchor="w", relief=tk.FLAT, bd=0,
                padx=8, pady=10, cursor="hand2",
                command=lambda k=key: self.show_tool(k)
            )
            btn.pack(fill=tk.X)
            btn.bind("<Enter>",  lambda e, b=btn: b.configure(bg=C["bg3"], fg=C["pearl"]))
            btn.bind("<Leave>",  lambda e, b=btn, k=key: b.configure(
                bg=C["bg4"] if self._active.get() == k else C["bg2"],
                fg=C["pearl"] if self._active.get() == k else C["muted"]
            ))
            self._nav_btns[key] = btn
            tk.Frame(sidebar, bg=C["border"], height=1).pack(fill=tk.X)

        tk.Label(sidebar, text="v1.0  •  AdiZenWorks Inc.",
                 bg=C["bg2"], fg="#333",
                 font=("Consolas", 7)).pack(side=tk.BOTTOM, pady=8)

        # ── CONTENT ──
        self.content = tk.Frame(body, bg=C["bg"])
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ── LOG BAR ──
        log_frame = tk.Frame(self.root, bg=C["bg2"], height=126)
        log_frame.pack(fill=tk.X, side=tk.BOTTOM)
        log_frame.pack_propagate(False)
        tk.Frame(log_frame, bg=C["crimson3"], height=1).pack(fill=tk.X)

        lhdr = tk.Frame(log_frame, bg=C["bg2"])
        lhdr.pack(fill=tk.X, padx=12, pady=(6, 2))
        tk.Label(lhdr, text="ACTIVITY LOG", bg=C["bg2"], fg=C["crimson"],
                 font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(lhdr, text="Clear", bg=C["bg2"], fg=C["muted"],
                  font=("Consolas", 7), relief=tk.FLAT, bd=0, cursor="hand2",
                  command=lambda: self._log_box.delete(1.0, tk.END)).pack(side=tk.RIGHT)

        self._log_box = tk.Text(log_frame, bg=C["bg"], fg="#555",
                                 font=("Consolas", 8), relief=tk.FLAT,
                                 height=5, wrap=tk.WORD, state=tk.NORMAL)
        self._log_box.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 8))
        for tag, fg in [("ok", C["success"]), ("err", C["crimson2"]),
                         ("warn", C["warn"]), ("info", C["info"]), ("ts", "#333")]:
            self._log_box.tag_config(tag, foreground=fg)

        self.show_tool("scanner")
        self.log("[SYSTEM] AdiZenWorks Toolkit V1 Desktop ready", "info")
        self.log("[SYSTEM] Select a tool from the sidebar to begin", "ok")

    # ═══════════════════════════════════════════════════════════
    # HELPERS
    # ═══════════════════════════════════════════════════════════
    def log(self, msg, tag=""):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self._log_box.config(state=tk.NORMAL)
        self._log_box.insert(tk.END, f"[{ts}] ", "ts")
        self._log_box.insert(tk.END, f"{msg}\n", tag or "")
        self._log_box.see(tk.END)

    def set_status(self, text, color=None):
        self.status_lbl.config(text=text, fg=color or C["success"])

    def show_tool(self, key):
        self._active.set(key)
        for k, b in self._nav_btns.items():
            if k == key:
                b.configure(bg=C["bg4"], fg=C["pearl"], padx=12)
            else:
                b.configure(bg=C["bg2"], fg=C["muted"], padx=8)
        for w in self.content.winfo_children():
            w.destroy()
        {
            "scanner":  self._panel_scanner,
            "auditor":  self._panel_auditor,
            "spider":   self._panel_spider,
            "hasher":   self._panel_hasher,
            "cracker":  self._panel_cracker,
            "inspector": self._panel_inspector,
            "filter":   self._panel_filter,
            "hello":    self._panel_hello,
        }[key]()

    # ── Widget helpers ──
    def _hdr(self, icon, title):
        hdr = tk.Frame(self.content, bg=C["bg"])
        hdr.pack(fill=tk.X, padx=24, pady=(20, 4))
        tk.Label(hdr, text=f"{icon}  {title}", bg=C["bg"], fg=C["pearl"],
                 font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT)
        tk.Frame(self.content, bg=C["crimson3"], height=1).pack(fill=tk.X, padx=24, pady=(2, 14))

    def _entry(self, label, default="", show=None):
        row = tk.Frame(self.content, bg=C["bg"])
        row.pack(fill=tk.X, padx=24, pady=4)
        tk.Label(row, text=label.upper(), bg=C["bg"], fg=C["muted"],
                 font=("Consolas", 7)).pack(anchor=tk.W)
        kw = dict(bg=C["bg3"], fg=C["pearl"], insertbackground=C["pearl"],
                  relief=tk.FLAT, bd=0, font=("Segoe UI", 10),
                  highlightthickness=1, highlightbackground=C["border2"],
                  highlightcolor=C["crimson"])
        if show:
            kw["show"] = show
        e = tk.Entry(row, **kw)
        e.pack(fill=tk.X, ipady=7, pady=2)
        if default:
            e.insert(0, default)
        return e

    def _combo(self, label, options, default=0):
        row = tk.Frame(self.content, bg=C["bg"])
        row.pack(fill=tk.X, padx=24, pady=4)
        tk.Label(row, text=label.upper(), bg=C["bg"], fg=C["muted"],
                 font=("Consolas", 7)).pack(anchor=tk.W)
        var = tk.StringVar(value=options[default])
        cb = ttk.Combobox(row, textvariable=var, values=options, state="readonly")
        cb.pack(fill=tk.X, pady=2)
        return var

    def _outbox(self):
        frame = tk.Frame(self.content, bg=C["bg"])
        frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=(8, 4))
        tk.Label(frame, text="OUTPUT", bg=C["bg"], fg=C["muted"],
                 font=("Consolas", 7)).pack(anchor=tk.W)
        box = scrolledtext.ScrolledText(
            frame, bg="#050505", fg="#777", font=("Consolas", 9),
            relief=tk.FLAT, wrap=tk.WORD,
            highlightthickness=1, highlightbackground=C["border"],
            highlightcolor=C["crimson3"]
        )
        box.pack(fill=tk.BOTH, expand=True, pady=2)
        for tag, fg in [("ok", C["success"]), ("err", C["crimson2"]),
                         ("warn", C["warn"]), ("info", C["info"]),
                         ("head", C["crimson"])]:
            box.tag_config(tag, foreground=fg)
        return box

    def _btnrow(self):
        row = tk.Frame(self.content, bg=C["bg"])
        row.pack(fill=tk.X, padx=24, pady=(10, 4))
        return row

    def _pbtn(self, parent, text, cmd):
        btn = tk.Button(parent, text=text,
                        bg=C["crimson3"], fg=C["pearl"],
                        activebackground=C["crimson"], activeforeground=C["pearl"],
                        font=("Segoe UI", 9, "bold"), relief=tk.FLAT, bd=0,
                        padx=18, pady=8, cursor="hand2", command=cmd)
        btn.pack(side=tk.LEFT, padx=(0, 8))
        btn.bind("<Enter>", lambda e: btn.configure(bg=C["crimson"]))
        btn.bind("<Leave>", lambda e: btn.configure(bg=C["crimson3"]))
        return btn

    def _sbtn(self, parent, text, cmd):
        btn = tk.Button(parent, text=text,
                        bg=C["bg3"], fg=C["muted"],
                        activebackground=C["bg4"], activeforeground=C["pearl"],
                        font=("Segoe UI", 9), relief=tk.FLAT, bd=0,
                        padx=14, pady=8, cursor="hand2", command=cmd)
        btn.pack(side=tk.LEFT, padx=(0, 8))
        return btn

    def _write(self, box, text, tag=""):
        box.config(state=tk.NORMAL)
        box.delete(1.0, tk.END)
        box.insert(tk.END, text, tag)

    def _append(self, box, text, tag=""):
        box.config(state=tk.NORMAL)
        box.insert(tk.END, text, tag)
        box.see(tk.END)

    def _thread(self, fn, *args):
        threading.Thread(target=fn, args=args, daemon=True).start()

    # ═══════════════════════════════════════════════════════════
    # TOOL PANELS
    # ═══════════════════════════════════════════════════════════

    # ── 1. PORT SCANNER ──────────────────────────────────────
    def _panel_scanner(self):
        self._hdr("🔌", "Port Scanner")
        target_e = self._entry("Target Host / IP", "192.168.1.1")
        ports_e  = self._entry("Ports (comma-separated)", "22,80,443,3306,8080")
        box = self._outbox()

        def run():
            target = target_e.get().strip()
            raw    = ports_e.get().strip() or "22,80,443"
            if not target:
                messagebox.showerror("Error", "Enter a target host.")
                return
            try:
                ports = [int(p.strip()) for p in raw.split(",")]
            except ValueError:
                messagebox.showerror("Error", "Ports must be comma-separated integers.")
                return
            self._write(box, f"[+] Scanning {target} — ports: {raw}\n\n")
            self.log(f"Port scan: {target}", "info")
            self.set_status("● SCANNING", C["warn"])
            try:
                results = adizenscanner.scan_ports(target, ports)
                open_ports = [p for p, s in results.items() if s == "OPEN"]
                for port, status in sorted(results.items()):
                    tag = "ok" if status == "OPEN" else "muted"
                    self._append(box, f"  {'OPEN' if status=='OPEN' else 'CLOSED':6}  :{port}\n",
                                 "ok" if status == "OPEN" else "")
                summary = f"\n[✓] Scan complete — {len(open_ports)} open / {len(results)} total"
                self._append(box, summary, "ok")
                self.log(f"Port scan done: {len(open_ports)} open on {target}", "ok")
            except Exception as e:
                self._append(box, f"\n[ERROR] {e}", "err")
                self.log(f"Scan error: {e}", "err")
            self.set_status("● READY")

        row = self._btnrow()
        self._pbtn(row, "⚡  Scan Ports", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 2. SYSTEM AUDITOR ────────────────────────────────────
    def _panel_auditor(self):
        self._hdr("🔍", "System Auditor")
        host_e = self._entry("Connectivity Check Host (optional)", "8.8.8.8")
        box = self._outbox()

        def run():
            self._write(box, "[+] Running system audit...\n\n")
            self.log("System audit started", "info")
            self.set_status("● AUDITING", C["warn"])
            try:
                info = adizenauditor.system_info()
                self._append(box, "── SYSTEM INFO ──────────────────────\n", "head")
                for k, v in info.items():
                    self._append(box, f"  {k:<22} {v}\n")

                check_host = host_e.get().strip() or "8.8.8.8"
                net = adizenauditor.network_check(check_host)
                self._append(box, f"\n── NETWORK CHECK ({check_host}) ────────\n", "head")
                if net is True:
                    self._append(box, "  Status               Connected\n", "ok")
                elif net is False:
                    self._append(box, "  Status               UNREACHABLE\n", "err")
                elif isinstance(net, dict):
                    for k, v in net.items():
                        self._append(box, f"  {k:<22} {v}\n",
                                     "ok" if str(v).lower() in ("connected", "true", "ok") else "")
                else:
                    self._append(box, f"  {net}\n")

                pkgs = adizenauditor.installed_packages()
                self._append(box, f"\n── INSTALLED PACKAGES (top {len(pkgs)}) ──\n", "head")
                for p in pkgs:
                    self._append(box, f"  {p}\n")

                self._append(box, "\n[✓] Audit complete\n", "ok")
                self.log("System audit complete", "ok")
            except Exception as e:
                self._append(box, f"\n[ERROR] {e}", "err")
                self.log(f"Audit error: {e}", "err")
            self.set_status("● READY")

        row = self._btnrow()
        self._pbtn(row, "⚡  Run Audit", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 3. WEB SPIDER ────────────────────────────────────────
    def _panel_spider(self):
        self._hdr("🕷", "Web Spider")
        url_e   = self._entry("Target URL", "https://example.com")
        limit_e = self._entry("Max Links", "20")
        box = self._outbox()

        def run():
            url   = url_e.get().strip()
            limit = int(limit_e.get().strip() or "20")
            if not url:
                messagebox.showerror("Error", "Enter a URL.")
                return
            self._write(box, f"[+] Crawling {url} (limit={limit})...\n\n")
            self.log(f"Spider: {url}", "info")
            self.set_status("● CRAWLING", C["warn"])
            try:
                links = adizenspider.crawl(url, limit)
                if links and links[0].startswith("Error:"):
                    self._append(box, links[0], "err")
                    self.log(f"Spider error: {links[0]}", "err")
                else:
                    self._append(box, f"── FOUND {len(links)} LINKS ──────────────────\n", "head")
                    for i, lnk in enumerate(links, 1):
                        self._append(box, f"  {i:3}.  {lnk}\n", "ok")
                    self._append(box, f"\n[✓] Crawl complete — {len(links)} links found\n", "ok")
                    self.log(f"Spider found {len(links)} links on {url}", "ok")
            except Exception as e:
                self._append(box, f"\n[ERROR] {e}", "err")
                self.log(f"Spider error: {e}", "err")
            self.set_status("● READY")

        row = self._btnrow()
        self._pbtn(row, "⚡  Start Spider", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 4. HASH GENERATOR ────────────────────────────────────
    def _panel_hasher(self):
        self._hdr("🔐", "Hash Generator")
        text_e = self._entry("Input Text", "Enter text to hash...")
        algo_v = self._combo("Algorithm",
                             ["sha256", "sha512", "sha1", "md5"], 0)
        box = self._outbox()

        def run():
            text = text_e.get().strip()
            algo = algo_v.get()
            if not text:
                messagebox.showerror("Error", "Enter text to hash.")
                return
            try:
                result = adizenhasher.generate_hash(text, algo)
                self._write(box, f"── {algo.upper()} HASH ──────────────────────────────\n", "head")
                self._append(box, f"\n  Input:   {text}\n")
                self._append(box, f"  Digest:  {result}\n", "ok")
                self.log(f"Hash [{algo.upper()}] generated", "ok")
            except Exception as e:
                self._write(box, f"[ERROR] {e}", "err")
                self.log(f"Hash error: {e}", "err")

        row = self._btnrow()
        self._pbtn(row, "⚡  Generate Hash", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 5. PASSWORD TESTER ───────────────────────────────────
    def _panel_cracker(self):
        self._hdr("💀", "Password Strength Tester")
        pw_e = self._entry("Password", show="●")
        box = self._outbox()

        def run():
            pw = pw_e.get()
            if not pw:
                messagebox.showerror("Error", "Enter a password.")
                return
            try:
                strength = adizencracker.check_strength(pw)
                color = {
                    "Very Strong": "ok", "Strong": "ok",
                    "Moderate": "warn", "Weak": "err"
                }.get(strength, "")
                self._write(box, f"── PASSWORD STRENGTH REPORT ──────────────\n\n", "head")
                self._append(box, f"  Password : {'*' * len(pw)}\n")
                self._append(box, f"  Length   : {len(pw)} characters\n")
                self._append(box, f"  Strength : {strength}\n\n", color)
                tips = []
                if len(pw) < 12:     tips.append("• Use at least 12 characters")
                if not any(c.isupper() for c in pw): tips.append("• Add uppercase letters")
                if not any(c.isdigit() for c in pw): tips.append("• Add numbers")
                import string
                if not any(c in string.punctuation for c in pw): tips.append("• Add special characters")
                if tips:
                    self._append(box, "  Suggestions:\n", "warn")
                    for t in tips:
                        self._append(box, f"    {t}\n", "warn")
                else:
                    self._append(box, "  ✓ Password meets all complexity requirements\n", "ok")
                self.log(f"Password check: {strength}", color or "info")
            except Exception as e:
                self._write(box, f"[ERROR] {e}", "err")
                self.log(f"Password error: {e}", "err")

        row = self._btnrow()
        self._pbtn(row, "⚡  Test Password", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 6. FILE INSPECTOR ────────────────────────────────────
    def _panel_inspector(self):
        self._hdr("📂", "File Inspector")
        path_e = self._entry("File Path", "/etc/hosts")
        box = self._outbox()

        def run():
            path = path_e.get().strip()
            if not path:
                messagebox.showerror("Error", "Enter a file path.")
                return
            self.log(f"Inspecting: {path}", "info")
            try:
                result = adizeninspector.inspect_file(path)
                if isinstance(result, str):
                    self._write(box, result, "err")
                    self.log(f"Inspector: {result}", "err")
                else:
                    self._write(box, f"── FILE METADATA ────────────────────────\n\n", "head")
                    for k, v in result.items():
                        self._append(box, f"  {k:<22} {v}\n")
                    self._append(box, "\n[✓] Inspection complete\n", "ok")
                    self.log(f"Inspector done: {path}", "ok")
            except Exception as e:
                self._write(box, f"[ERROR] {e}", "err")
                self.log(f"Inspector error: {e}", "err")

        row = self._btnrow()
        self._pbtn(row, "⚡  Inspect File", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 7. DATA FILTER ───────────────────────────────────────
    def _panel_filter(self):
        self._hdr("🧹", "Data Filter / Sanitizer")

        # Multi-line input
        in_frame = tk.Frame(self.content, bg=C["bg"])
        in_frame.pack(fill=tk.X, padx=24, pady=4)
        tk.Label(in_frame, text="INPUT TEXT (HTML/RAW)", bg=C["bg"], fg=C["muted"],
                 font=("Consolas", 7)).pack(anchor=tk.W)
        input_box = tk.Text(in_frame, bg=C["bg3"], fg=C["pearl"],
                            insertbackground=C["pearl"],
                            font=("Segoe UI", 10), relief=tk.FLAT, height=5,
                            wrap=tk.WORD,
                            highlightthickness=1, highlightbackground=C["border2"],
                            highlightcolor=C["crimson"])
        input_box.pack(fill=tk.X, pady=2)
        input_box.insert(tk.END, "<p>Hello <b>World</b>!</p>  Some  extra   spaces.")

        box = self._outbox()

        def run():
            text = input_box.get("1.0", tk.END).strip()
            if not text:
                messagebox.showerror("Error", "Enter text to sanitize.")
                return
            try:
                result = adizenfilter.sanitize(text)
                self._write(box, "── SANITIZED OUTPUT ─────────────────────\n\n", "head")
                self._append(box, result + "\n", "ok")
                self.log("Data filter applied", "ok")
            except Exception as e:
                self._write(box, f"[ERROR] {e}", "err")
                self.log(f"Filter error: {e}", "err")

        row = self._btnrow()
        self._pbtn(row, "⚡  Sanitize", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))

    # ── 8. ENV CHECK ─────────────────────────────────────────
    def _panel_hello(self):
        self._hdr("👋", "Environment Check")
        box = self._outbox()

        def run():
            import sys
            import platform
            self._write(box, "── ENVIRONMENT INFO ─────────────────────\n\n", "head")
            self._append(box, f"  Python Version   {sys.version.split()[0]}\n", "ok")
            self._append(box, f"  Platform         {platform.system()} {platform.release()}\n")
            self._append(box, f"  Machine          {platform.machine()}\n")
            self._append(box, f"  Processor        {platform.processor() or 'N/A'}\n")
            self._append(box, f"  Python Path      {sys.executable}\n")
            self._append(box, "\n── MODULE STATUS ────────────────────────\n\n", "head")
            mods = ["adizenscanner", "adizenauditor", "adizenspider",
                    "adizenhasher", "adizencracker", "adizeninspector",
                    "adizenfilter", "adizenhello"]
            for m in mods:
                ok = MODULES_OK
                self._append(box, f"  {'✓' if ok else '✗'}  {m}\n", "ok" if ok else "err")
            self._append(box, f"\n[✓] Environment check complete\n", "ok")
            self.log("Environment check done", "ok")

        row = self._btnrow()
        self._pbtn(row, "⚡  Run Check", lambda: self._thread(run))
        self._sbtn(row, "Clear", lambda: box.delete(1.0, tk.END))


# ── ENTRY POINT ───────────────────────────────────────────────
def main():
    root = tk.Tk()
    AdiZenV1Desktop(root)
    root.mainloop()


if __name__ == "__main__":
    main()
