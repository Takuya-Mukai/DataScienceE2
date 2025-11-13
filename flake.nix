{
  description = "A flake dataAnalysis";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    myDataAnalysisFlake.url = "github:Takuya-Mukai/nix-overlay";
  };

  outputs =
    {
      self,
      nixpkgs,
      myDataAnalysisFlake,
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forAllSystems =
        f:
        builtins.listToAttrs (
          map (system: {
            name = system;
            value = f system;
          }) supportedSystems
        );
    in
    {
      devShells = forAllSystems (system: {
        default = myDataAnalysisFlake.devShells.${system}.dataAnalysis;
      });
    };
}
