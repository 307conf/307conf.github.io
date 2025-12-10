+++
title = "Persistent Vulnerabilities in the Linux Kernel CAN BCM Protocol: An Exploitation and Discovery Analysis"
date = 2025-12-13T10:50:00-03:00
authors = ["anderson-nascimento"]
track = "main"
short_description = "Analysis of persistent flaws in the Linux kernel CAN BCM protocol, practical exploitation, and challenges in the patching process."
summary = "Anderson Nascimento shares his experience discovering and exploiting multiple vulnerabilities in the Linux kernel’s CAN BCM protocol, discussing persistent flaws, insecurity patterns, and limitations in the remediation process."
logo = "/images/speakers/anderson-nascimento.png"
weight = 1
+++

In 2020, Anderson Nascimento began researching the CAN BCM protocol in the Linux kernel while developing an exploit for a use-after-free read vulnerability. Although fixed upstream, the flaw still affected recent versions of several Linux distributions, revealing significant gaps in the ecosystem’s patching process. His exploit demonstrated the severity of the issue by allowing an unprivileged user to access privileged files and read memory addresses from arbitrary processes.

Years later, when revisiting the same component, Anderson identified a pattern of vulnerabilities. A new flaw — also fixed upstream — remained present in the latest versions of popular distributions. He then developed another exploit capable of leaking privileged information and bypassing kernel security mitigations.

While documenting this second vulnerability, he noticed that the applied fix was ineffective, making it possible to exploit the same behavior again and leading to the discovery of a third flaw — this time a 0-day in the CAN BCM procfs component. He also identified a second 0-day unrelated to the protocol’s procfs.

All vulnerabilities were reported and later fixed by the kernel maintainers.  
The presentation details Anderson’s hands-on experience discovering, exploiting, and reporting these flaws in the CAN BCM protocol, including challenges in the patch pipeline, exploitation techniques, and lessons from auditing the Linux kernel.
