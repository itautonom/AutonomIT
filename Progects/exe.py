#py -m auto_py_to_exe

import tkinter as tk

TEXT = """PORTFOLIO
==================================================
TEAM SERVICES
==================================================

The team undertakes large and complex projects, including long-term development.
We close most of the tasks on a turnkey basis, and select the team for the project.

Development:
- Programs and applications
- Websites and web applications
- Online stores and marketplaces
- SaaS, CRM, ERP and corporate portals
- Games and game projects (PC, mobile, Web, 2D/3D, multiplayer)
- Mobile applications (iOS, Android, cross‑platform)
- Automation of tasks and business processes
- Bots and parsers
- APIs and integrations
- Refinement and optimization of existing projects
- Bug fixing and technical support

Development of a project from scratch:

- Brief and task analysis
- Prototype and technical requirements
- Design and layout
- Development
- Testing
- Publication and setup
- Support and development

AI solutions:

- Chatbots and assistants
- Content generation
- Data analysis
- Support automation
- AI implementation in existing projects

Design:
- UI/UX design
- Branding, logos
- Prototypes and design systems
- Presentations and visual design

DevOps and infrastructure:

- Project deployment
- CI/CD, Docker, Kubernetes
- Server, domain, SSL, and backup setup
- Monitoring and scaling

SEO and traffic:
- SEO audit and promotion
- Content and content plan
- Advertising and analytics
- Publishing on Google and Yandex

Support and development:
- Project maintenance
- Regular updates
- Improvements and bug fixes
- Consultations and training
- Blog management

Additional:
- Blog creation
- Technical support
- Regular updates
- Further development of the project
- Outsourcing / outstaffing — dedicated developers and teams

==================================================
TEAM TECHNOLOGIES
==================================================

Programming languages:
- Python, C#, C++, Java, JavaScript / TypeScript
- PHP, Go, Rust, Kotlin, Swift, SQL, Bash, PowerShell

Frontend:
- HTML5, CSS3, SCSS, Tailwind, Bootstrap
- React, Vue, Angular, Svelte, Next.js, Nuxt

Backend:
- Django, Flask, FastAPI
- Node.js, Express, NestJS
- ASP.NET, Spring, Laravel

Mobile development:
- Android, iOS
- Flutter, React Native, Kotlin, Swift

Games:
- Unity, Unreal Engine, Godot, Pygame
- 2D/3D, gameplay, multiplayer, monetization

Databases:
- PostgreSQL, MySQL, SQLite, MS SQL
- MongoDB, Redis, Firebase, Supabase

DevOps and infrastructure:
- Docker, Kubernetes, CI/CD
- GitHub Actions, GitLab CI
- Linux, Nginx, Apache, VPS
- AWS, GCP, Azure
- Domains, SSL, backups, GIT

APIs and integrations:
- REST, GraphQL, WebSocket
- Telegram Bot API, Discord API, VK API
- Payment systems, OAuth
- CRM, 1C, Google Sheets

AI and data:
- OpenAI API, LLM, prompt engineering
- Data parsing and processing
- Pandas, NumPy
- PyTorch, TensorFlow
- ML, NLP, CV
- Automation

Design:
- UI/UX, Figma
- Responsive design, prototypes
- Branding, logos, presentations

SEO and marketing:
- SEO audit, semantics, meta tags, sitemap, robots, Schema.org
- Google Analytics, Yandex.Metrica
- Advertising, content plan

Security:
- Code and security audit
- Protection against SQL injections, XSS, CSRF
- Monitoring and backups
- Testing

Management:
- PM, Agile, Scrum, Kanban
- Jira, Trello, Notion
- Documentation

==================================================
FIRMWARE AND MICROCONTROLLERS
==================================================

Services:

- Firmware development for microcontrollers
  (Arduino, ESP32, STM32, AVR, PIC, RP2040)
- Firmware for Raspberry Pi and single‑board computers
- Work with peripherals: sensors, motors, servos,
  relays, displays, buttons, encoders
- Communication protocols: UART, I2C, SPI, CAN, Modbus, 1-Wire
- Wireless connection: Wi-Fi, Bluetooth/BLE, LoRa, RF
- Firmware of ready-made devices (rooters, cameras, printers)
- Device recovery after failed firmware
- Optimization for low memory and low power consumption
- Bootloader and offline updates (SD, USB, local server)
- Debugging: JTAG, SWD, ST-Link, logic analyzers

Technologies:

- Languages: C, C++, MicroPython, CircuitPython, assembly language
- Environments: Arduino IDE, PlatformIO, STM32CubeIDE, MPLAB, VS Code
- OS: FreeRTOS, Zephyr, bare-metal
- Platforms: Arduino, ESP32 / ESP8266, STM32, RP2040, ATmega, PIC
- PCB design: KiCad, EasyEDA

Offline direction:

- Firmware without clouds and external services
- Fully autonomous devices
- Updates without an internet connection
- Operation in isolated and industrial systems

And other technologies — we select the stack to suit the project.

==================================================
HOW WE WORK
==================================================

1. Brief and task discussion
2. Assessment and technical specifications
3. Prototype and design
4. Development
5. Testing
6. Launch and configuration
7. Support and development

Work formats:
- Fixed price
- Hourly payment
- Subscription / long-term contract

Guarantees:
- Agreement
- Work by stages
- Edits within the framework of the TOR
- Support after the completion of the project

==================================================
WORKING CONDITIONS OF THE TEAM
==================================================

1. We receive the application
2. We discuss the price and terms
3. We do the work according to the TOR
4. Showing the result
5. We receive the payment
6. The project goes to you
7. To continue — updates, support,
   development — we are negotiating a contract

--------------------------------------------------

Everything is transparent and step-by-step.
The project is completely yours after payment.
Further support is provided under a separate agreement.
==================================================
EDITS AND DEADLINES
==================================================

EDITS

- 2 free rounds of edits within the TOR
- Edits in excess of the TOR — are paid separately
- Change of TK in the process = revision of the price and terms
- Minor edits along the way — free of charge

--------------------------------------------------
DEADLINES
--------------------------------------------------

- Deadlines are fixed after the approval of the TOR
- Delays caused by the customer (no response, no
  materials) the deadline is being shifted
- Urgency ("it is necessary yesterday") — margin +30-100%
- We will notify you in advance about any delays.
- If we are late due to our own fault, you will receive a 30% discount.

==================================================
CURRENT SERVICES
==================================================
- Single‑page website — from 1,000 RUB (5/5)
- Multi‑page website — from 2,000 RUB (5/5)
- Windows program (.exe) — from 3,000 RUB (4/5)
- Special tasks / with AI — from 1,500 ₽ or in person (3/5)

Conditions:

- Websites — on a free domain. Paid domain — by agreement.
- Deadlines — by agreement.
- First, a test; after payment, the source code.
==================================================
contacts
==================================================

Telegram: @elliotandersonela
Telegram channel: https://t.me/AutonombySa1DeN
Website: https://itautonom.netlify.app/
Githab: https://github.com/itautonom/AutonomIT
"""


HEADINGS = {
    "PORTFOLIO",
    "TEAM SERVICES",
    "TEAM TECHNOLOGIES",
    "FIRMWARE AND MICROCONTROLLERS",
    "HOW WE WORK",
    "WORKING CONDITIONS OF THE TEAM",
    "EDITS AND DEADLINES",
    "EDITS",
    "DEADLINES",
    "CURRENT SERVICES",
    "CONTACTS",
}


class PortfolioViewer:
    def __init__(self, root):
        self.root = root
        root.title("AUTONOM — Портфолио")
        root.geometry("1050x820")
        root.minsize(650, 500)
        root.configure(bg="#101410")

        header = tk.Frame(root, bg="#101410")
        header.pack(fill="x", padx=22, pady=(16, 8))

        tk.Label(
            header, text="AUTONOM", bg="#101410", fg="#76e36b",
            font=("Segoe UI", 19, "bold")
        ).pack(side="left")

        tk.Label(
            header, text="ПОРТФОЛИО КОМАНДЫ", bg="#101410", fg="#aab5a8",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=(14, 0), pady=(7, 0))

        self.status = tk.Label(
            header, text="Прокручивайте текст колесом мыши или полосой справа",
            bg="#101410", fg="#829082", font=("Segoe UI", 9)
        )
        self.status.pack(side="right", pady=(7, 0))

        body = tk.Frame(
            root, bg="#1a211a", highlightthickness=1, highlightbackground="#304330"
        )
        body.pack(fill="both", expand=True, padx=18, pady=(4, 18))

        self.text = tk.Text(
            body, wrap="word", undo=False, padx=24, pady=20,
            bg="#151b15", fg="#e3e9e1", insertbackground="#76e36b",
            selectbackground="#315b35", selectforeground="#ffffff",
            relief="flat", borderwidth=0, spacing1=2, spacing3=3,
            font=("Consolas", 11), state="normal"
        )
        scrollbar = tk.Scrollbar(
            body, orient="vertical", command=self.text.yview,
            bg="#263326", troughcolor="#151b15",
            activebackground="#76e36b", relief="flat"
        )
        self.text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y", padx=(0, 5), pady=5)
        self.text.pack(side="left", fill="both", expand=True, padx=(5, 0), pady=5)

        self.text.insert("1.0", TEXT)
        self.text.tag_configure(
            "heading", foreground="#76e36b",
            font=("Segoe UI", 13, "bold"), spacing1=8, spacing3=5
        )
        self.text.tag_configure(
            "subheading", foreground="#b6e6ad",
            font=("Segoe UI", 11, "bold"), spacing1=7, spacing3=2
        )
        self.text.tag_configure(
            "separator", foreground="#4d754b",
            font=("Consolas", 10)
        )

        self._apply_tags()
        self.text.configure(state="disabled")

        self.text.bind("<MouseWheel>", self._on_mousewheel)
        self.text.bind("<Button-4>", lambda e: self.text.yview_scroll(-3, "units"))
        self.text.bind("<Button-5>", lambda e: self.text.yview_scroll(3, "units"))
        self.text.bind("<Control-a>", self._select_all)
        self.text.bind("<Control-A>", self._select_all)

    def _apply_tags(self):
        for line_no, line in enumerate(TEXT.splitlines(), start=1):
            stripped = line.strip()
            if not stripped:
                continue
            start = f"{line_no}.0"
            end = f"{line_no}.end"
            chars = set(stripped)
            if chars == {"="} or (chars == {"-"} and len(stripped) > 3):
                self.text.tag_add("separator", start, end)
            elif stripped.upper() in HEADINGS:
                self.text.tag_add("heading", start, end)
            elif stripped.endswith(":") and not stripped.startswith("-"):
                self.text.tag_add("subheading", start, end)

    def _on_mousewheel(self, event):
        self.text.yview_scroll(int(-event.delta / 120), "units")
        return "break"

    def _select_all(self, event=None):
        self.text.configure(state="normal")
        self.text.tag_add("sel", "1.0", "end")
        self.text.configure(state="disabled")
        return "break"


if __name__ == "__main__":
    window = tk.Tk()
    app = PortfolioViewer(window)
    window.mainloop()
